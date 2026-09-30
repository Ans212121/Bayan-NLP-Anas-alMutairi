"""Correction contract tests with a fake runtime; these are not ML quality measurements."""
import ast
import json
import uuid
from pathlib import Path
from time import perf_counter_ns
from typing import Literal
import numpy as np
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field, field_validator
from bayan.correction_preprocessing import prepare, VERSION
from bayan.serving import ServingManifest, build_prediction_response, validate_request_text

def test_shared_preprocessing_masks_pii_and_preserves_arabic_letters():
    source='  إِدارة  على هاتف 0501234567 أو demo@example.org  '
    cleaned=prepare(source)
    assert cleaned=='إِدارة على هاتف <PHONE> أو <EMAIL>'
    assert prepare(cleaned)==cleaned

class FakeTokenizer:
    def __call__(self,texts,**kwargs):
        return {'input_ids':np.array([[len(t),1] for t in texts]),'attention_mask':np.ones((len(texts),2))}
class FakeSession:
    def run(self,names,inputs):
        x=inputs['input_ids'][:,0]%2
        return [np.stack([1-x,x],axis=1).astype(float)]

def test_batch_endpoint_order_contract_and_invalid_inputs():
    nb=json.loads((Path(__file__).parents[1]/'notebooks/08_optimization_serving.ipynb').read_text(encoding='utf8'))
    sources=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
    request_src=next(s for s in sources if s.startswith('class ClassifyRequest'))
    batch_src=next(s for s in sources if s.startswith('# A real bounded batch endpoint'))
    app=FastAPI()
    ns=dict(BaseModel=BaseModel,Field=Field,field_validator=field_validator,Literal=Literal,
        validate_request_text=validate_request_text,app=app,prepare=prepare,np=np,
        tokenizer=FakeTokenizer(),selected_session=FakeSession(),MAX_LENGTH=64,
        perf_counter_ns=perf_counter_ns,uuid=uuid,LABEL_MAP={0:'even',1:'odd'},
        build_prediction_response=build_prediction_response,
        manifest=ServingManifest('fake','test',VERSION,'fake',{0:'even',1:'odd'},'0'*64),
        softmax=lambda a:np.exp(a)/np.exp(a).sum(axis=-1,keepdims=True))
    req=ast.parse(request_src).body[0]
    exec(compile(ast.Module(body=[req],type_ignores=[]),'<request>','exec'),ns)
    body=[x for x in ast.parse(batch_src).body if isinstance(x,(ast.ClassDef,ast.FunctionDef))][:2]
    exec(compile(ast.Module(body=body,type_ignores=[]),'<batch>','exec'),ns)
    with TestClient(app) as client:
        response=client.post('/v1/classify-batch',json={'items':[{'text':'hi','language':'en'},{'text':'مرحبا','language':'ar'}]})
        assert response.status_code==200
        result=response.json()
        assert result['batch_size']==2
        assert [x['prediction']['label'] for x in result['items']]==['even','odd']
        assert [x['language'] for x in result['items']]==['en','ar']
        for payload in [{'items':[]},{'items':[{'text':'   '}]},{'items':[{'text':'ok','language':'xx'}]},{'items':[{'text':'ok'}]*17}]:
            assert client.post('/v1/classify-batch',json=payload).status_code==422
