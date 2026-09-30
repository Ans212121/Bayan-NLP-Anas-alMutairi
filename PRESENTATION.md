# PRESENTATION — Bayan | عرض بيان

**GitHub username / معرف المتدرب:** Ans212121

## 1. Problem and user | المشكلة والمستخدم

Bayan is an educational bilingual NLP project for Arabic and English feedback.

- User: student/trainer reviewing an NLP workflow.
- Input: Arabic or English educational text.
- Scope: privacy-aware preprocessing, topic/sentiment, NER, QA, semantic search, evaluation and serving.
- Non-goal: production or high-impact use without additional validation.

## 2. Architecture | المعمارية

See `README.md`.

`AR/EN text → display/raw copy + PII masking → versioned preprocessing → tokenizer/embeddings → Transformer encoder → topic/sentiment/NER/QA heads`

Search path:

`preprocessed query → multilingual sentence embedding → L2 → FAISS → cross-encoder re-ranking → unified evidence`

Attention maps are descriptive and are not treated as causal explanations.

## 3. Demonstration | التطبيق

Preserved examples:
- QA valid span: answer `الرياض` — `reports/observed_ner_qa.json`
- QA no-answer: `no_answer_in_context` — `reports/observed_ner_qa.json`
- Arabic profile: 4/4 golden cases — `reports/observed_arabic_profile.json`
- Search manifest: 24 vectors, 384 dimensions, L2 + IndexFlatIP — `reports/observed_search_manifest.json`

Corrected-run demonstrations to show after Run All:
- separate sentiment prediction + Macro-F1 evidence;
- PROJECT_ARTIFACT service response;
- batch endpoint extension.

## 4. Measured evidence | الدليل المقاس

Preserved evidence:
- Topic test Macro-F1: **0.8667**
- Topic test accuracy: **0.8750**
- NER strict F1: **0.5714**
- Search Recall@3: **1.0000**
- Core re-ranking MRR@3: **0.6667 → 0.7222**
- Behavioural course-fixture pass rate: **3/6**

Slice/error evidence:
- `reports/day3_slice_report.csv`
- `reports/day3_error_taxonomy.csv`
- `reports/day3_evaluation_fixture.json`

Day 4 final project metrics are not presented until the PROJECT_ARTIFACT rerun is complete.

## 5. Decision and ownership | القرار والمساهمة

### My concrete contribution
I implemented and ran the combined student workflow, including preprocessing/token metrics, attention checks, grouped topic fine-tuning, NER/QA, Arabic profiles, semantic retrieval and evaluation/error analysis. The corrected official notebooks are reorganised from that work.

### Required extension
Chosen extension: **batch endpoint**.

Why:
- cross-encoder re-ranking is already part of the core search requirement;
- batch inference is an allowed measured extension.

Corrected Notebook 08 will compare sequential calls with a true batch model call, verify prediction agreement, measure throughput/latency trade-off and write `reports/extension_batch_endpoint.json`.

### Code decision I can explain
For semantic search I use L2-normalised multilingual embeddings with FAISS `IndexFlatIP`, and I tune the no-answer threshold on validation data only to avoid test leakage.

The talk is five minutes plus two minutes of individual verification; up to five slides or equivalent.
