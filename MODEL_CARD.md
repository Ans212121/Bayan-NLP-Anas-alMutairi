from pathlib import Path
text = """# بطاقة نموذج بيان | Bayan Model Card

**Student:** Anas Ibrahim Al-Mutairi  
**Program:** Applied Natural Language Processing  
**Program Code:** SDA-AIE-211  
**Project:** Bayan  
**Trainer:** Meaad Al-Marri  
**Repository:** `Ans212121/Bayan-NLP-anas-al-mutairi`  
**Current reference commit:** `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`

> هذه البطاقة توثق الـ artefacts التي ظهرت في أدلة المشروع الحالية.  
> الأرقام الموسومة `MEASURED_SMOKE` هي نتائج تشغيل مقاسة على بيانات تعليمية صغيرة، وليست ادعاءً بجاهزية إنتاجية.

## 1) Topic Classification

### Model details
- Name/version: `Bayan Topic Classifier`
- Base checkpoint: `distilbert/distilbert-base-multilingual-cased`
- Task: Topic classification
- License/source: Hugging Face model checkpoint + Bayan Applied NLP course dataset
- Commit SHA: `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`
- Owner/contact role: Anas Ibrahim Al-Mutairi — student/project owner
- Result type: `MEASURED_SMOKE`

### Intended use
- الاستخدام المقصود: تصنيف أمثلة نصية عربية/إنجليزية إلى موضوعات الدورة.
- المستخدمون المقصودون: الطالب والمدرب لأغراض التدريب والتقييم الأكاديمي.
- خارج النطاق: الاستخدام الإنتاجي أو القرارات عالية التأثير.

### Data and preprocessing
- Dataset ID/version: Bayan course classification dataset
- Languages/variants: Arabic + English
- Split strategy: grouped train/validation/test split; seed `42`
- PII policy: mask emails as `<EMAIL>` and Saudi mobile-number patterns as `<PHONE>`
- Preprocessing profile/version/backend: protected two-copy preprocessing; raw text preserved separately from model text
- Tokenizer/embedding model: tokenizer corresponding to `distilbert/distilbert-base-multilingual-cased`

### Evaluation
| metric/slice | n | result | uncertainty | evidence file |
|---|---:|---:|---|---|
| Validation Macro-F1 | small course split | 1.0000 | small validation set | `reports/observed_classification.json` |
| Test Macro-F1 | 8 test rows | 0.8667 | small test set | `reports/observed_classification.json` |
| Test accuracy | 8 test rows | 0.8750 | small test set | `reports/observed_classification.json` |
| Baseline test Macro-F1 | 8 test rows | 0.7333 | small test set | `reports/observed_classification.json` |

### Behavioural checks
| capability | pass rate | known failure |
|---|---:|---|
| Split isolation / leakage checks | PASS | Small dataset limits confidence |
| Core notebook validation | PASS | Not a production-quality estimate |

### Limitations and risks
1. Small synthetic/course dataset.
2. Small validation set was used for epoch selection.
3. Metrics are educational smoke-test results, not production estimates.

### Ethical and privacy notes
- Course/public or synthetic examples only.
- PII masking is applied to email and Saudi mobile-number patterns.
- No production-readiness claim is made.

### Reproduction
1. افتح notebook: `bayan_NLP_ANAS_AI_Mutairi.ipynb`.
2. استخدم runtime/device: Google Colab / CPU.
3. ثبت النسخ من `requirements.txt`.
4. شغّل الخلايا بالترتيب من commit: `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`.
5. قارن النتيجة مع: `reports/observed_classification.json`.

---

## 2) Sentiment Classification

### Model details
- Name/version: `Bayan Sentiment Head`
- Base checkpoint: multilingual Transformer workflow used in the Bayan course
- Task: Sentiment classification
- License/source: Bayan Applied NLP course materials
- Commit SHA: `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`
- Owner/contact role: Anas Ibrahim Al-Mutairi — student/project owner

### Intended use
- الاستخدام المقصود: تجربة sentiment classification ضمن مختبرات Bayan التعليمية.
- المستخدمون المقصودون: الطالب والمدرب.
- خارج النطاق: تحليل مشاعر مستخدمين حقيقيين لأغراض إنتاجية.

### Data and preprocessing
- Dataset ID/version: Bayan course classification dataset
- Languages/variants: Arabic + English
- Split strategy: grouped course split
- PII policy: same protected preprocessing policy used by the project
- Preprocessing profile/version/backend: protected two-copy preprocessing
- Tokenizer/embedding model: multilingual Transformer tokenizer used by the course workflow

### Evaluation
| metric/slice | n | result | uncertainty | evidence file |
|---|---:|---:|---|---|
| Separate sentiment metric export | — | Not separately preserved in the current evidence package | Do not infer a score | `notebooks/03_sentiment_completion.ipynb` |

### Behavioural checks
| capability | pass rate | known failure |
|---|---:|---|
| Notebook completion artefact present | Present | Separate measured sentiment summary was not exported into current reports |

### Limitations and risks
1. No separate sentiment score is claimed without preserved evidence.
2. Small educational dataset.
3. Not validated for production sentiment analysis.

### Ethical and privacy notes
- Educational use only.
- Do not infer sensitive traits or profile real individuals from sentiment output.
- No production claim.

### Reproduction
1. افتح notebook: `notebooks/03_sentiment_completion.ipynb`.
2. استخدم runtime/device المناسب للمشروع.
3. ثبت النسخ من `requirements.txt`.
4. شغّل الخلايا بالترتيب.
5. سجّل أي metric جديد في ملف evidence مستقل قبل اعتماده.

---

## 3) Named Entity Recognition (NER)

### Model details
- Name/version: `Bayan NER`
- Base checkpoint: `distilbert/distilbert-base-multilingual-cased`
- Task: Named Entity Recognition with BIO/subword alignment
- License/source: Hugging Face checkpoint + Bayan Applied NLP course dataset
- Commit SHA: `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`
- Owner/contact role: Anas Ibrahim Al-Mutairi — student/project owner
- Result type: `MEASURED_SMOKE`

### Intended use
- الاستخدام المقصود: تعلم وتقييم NER مع BIO alignment وحدود الكيانات.
- المستخدمون المقصودون: الطالب والمدرب.
- خارج النطاق: استخراج كيانات من بيانات حساسة أو تشغيل إنتاجي دون مراجعة بشرية.

### Data and preprocessing
- Dataset ID/version: Bayan course NER dataset
- Languages/variants: Arabic/English course fixtures
- Split strategy: course-provided training/evaluation workflow
- PII policy: protected preprocessing; do not upload real PII
- Preprocessing profile/version/backend: BIO/subword alignment + strict entity-boundary validation
- Tokenizer/embedding model: `distilbert/distilbert-base-multilingual-cased`

### Evaluation
| metric/slice | n | result | uncertainty | evidence file |
|---|---:|---:|---|---|
| Precision | 3 predicted entities | 0.6667 | very small entity count | `reports/observed_ner_qa.json` |
| Recall | 4 true entities | 0.5000 | very small entity count | `reports/observed_ner_qa.json` |
| Strict entity F1 | 4 true / 3 predicted | 0.5714 | very small entity count | `reports/observed_ner_qa.json` |
| Final training loss | 12 epochs | 0.0427 | smoke-run context | `PROJECT_SUMMARY.json` |

### Behavioural checks
| capability | pass rate | known failure |
|---|---:|---|
| BIO/subword alignment | PASS | Small evaluation sample |
| Strict entity-boundary test | PASS | Boundary quality is not a production estimate |

### Limitations and risks
1. Very small number of evaluated entities.
2. Short educational training run.
3. Entity quality is not representative of production data.

### Ethical and privacy notes
- Do not process real personal/sensitive data without additional safeguards.
- PII masking is part of the project preprocessing.
- Human review is required for real-world use.

### Reproduction
1. افتح notebook: `bayan_NLP_ANAS_AI_Mutairi.ipynb`.
2. استخدم Google Colab / CPU.
3. ثبت النسخ من `requirements.txt`.
4. شغّل NER cells بالترتيب.
5. قارن النتيجة مع: `reports/observed_ner_qa.json`.

---

## 4) Extractive Question Answering (QA)

### Model details
- Name/version: `Bayan Extractive QA`
- Base checkpoint: `distilbert/distilbert-base-multilingual-cased`
- Task: Extractive Question Answering with no-answer handling
- License/source: Hugging Face checkpoint + Bayan Applied NLP course fixtures
- Commit SHA: `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`
- Owner/contact role: Anas Ibrahim Al-Mutairi — student/project owner
- Result type: `MEASURED_SMOKE`

### Intended use
- الاستخدام المقصود: توضيح extractive QA وtoken-offset alignment وno-answer decisions.
- المستخدمون المقصودون: الطالب والمدرب.
- خارج النطاق: أنظمة إجابة إنتاجية أو استخدامات تتطلب دقة موثوقة عالية.

### Data and preprocessing
- Dataset ID/version: Bayan course QA dataset
- Languages/variants: Arabic/English course examples
- Split strategy: course fixture workflow
- PII policy: no real PII; protected preprocessing where applicable
- Preprocessing profile/version/backend: offset-to-token mapping and bounded span extraction
- Tokenizer/embedding model: `distilbert/distilbert-base-multilingual-cased`

### Evaluation
| metric/slice | n | result | uncertainty | evidence file |
|---|---:|---:|---|---|
| QA training loss | 3 optimizer steps | 3.6451 | short smoke run | `reports/observed_ner_qa.json` |
| Valid span test | fixture | PASS | course fixture | `reports/observed_ner_qa.json` |
| No-answer handling | fixture | PASS | course fixture | `reports/observed_ner_qa.json` |
| Example extracted answer | fixture | `الرياض` | fixture only | `reports/observed_ner_qa.json` |

### Behavioural checks
| capability | pass rate | known failure |
|---|---:|---|
| Offset-to-token alignment | PASS | Limited fixture coverage |
| No-answer behaviour | PASS | Not a production-calibrated abstention system |

### Limitations and risks
1. Very short training smoke run.
2. Fixture-based evaluation rather than broad QA benchmark.
3. No production-quality EM/F1 claim is made.

### Ethical and privacy notes
- Educational/course-fixture use only.
- No sensitive documents should be submitted without additional controls.
- Human verification is required for real-world answers.

### Reproduction
1. افتح notebook: `bayan_NLP_ANAS_AI_Mutairi.ipynb`.
2. استخدم Google Colab / CPU.
3. ثبت النسخ من `requirements.txt`.
4. شغّل QA cells بالترتيب.
5. قارن النتيجة مع: `reports/observed_ner_qa.json`.

---

## 5) Semantic Embeddings and Re-ranker

### Model details
- Name/version: `Bayan Bilingual Semantic Search`
- Base embedding checkpoint: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Re-ranker checkpoint: `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`
- Task: Bilingual semantic retrieval + cross-encoder re-ranking
- License/source: Hugging Face model sources + Bayan course search dataset
- Commit SHA: `4e9fa8c7b1376dfd739d13bbd9b7e3738d3d6ed5`
- Owner/contact role: Anas Ibrahim Al-Mutairi — student/project owner
- Result type: `MEASURED_SMOKE`

### Intended use
- الاستخدام المقصود: استرجاع دلالي ثنائي اللغة وتجربة re-ranking على بيانات Bayan.
- المستخدمون المقصودون: الطالب والمدرب.
- خارج النطاق: محرك بحث إنتاجي أو استخدام يتطلب ضمانات جودة واسعة.

### Data and preprocessing
- Dataset ID/version: `bayan_day3_cases.csv`
- Dataset SHA256: `7708cbe884a3c268d24ed2cb87ad2f0a8b64b2e6fa6b37a32393b6ae3bd50e5b`
- Languages/variants: Arabic + English
- Split strategy: validation-only threshold tuning followed by frozen-threshold test
- PII policy: no real PII; project masking rules apply
- Preprocessing profile/version/backend: `arabic-search/1.0.0 + english-nfc-whitespace/1.0.0`
- Embedding model: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Embedding dimension: `384`
- Vector normalisation: `L2`
- Index: `FAISS IndexFlatIP`
- Vector count: `24`

### Evaluation
| metric/slice | n | result | uncertainty | evidence file |
|---|---:|---:|---|---|
| Recall@3 | course test queries | 1.0000 | small dataset | `PROJECT_SUMMARY.json` |
| MRR@3 before re-ranking | 6 answerable queries | 0.6667 | small query set | `reports/observed_reranking_display.json` |
| MRR@3 after re-ranking | 6 answerable queries | 0.7222 | small query set | `reports/observed_reranking_display.json` |
| MRR@3 delta | 6 answerable queries | +0.0556 | small query set | `reports/observed_reranking_display.json` |
| Validation threshold | validation set | 0.4592 | validation-only tuning | `PROJECT_SUMMARY.json` |
| Frozen-threshold no-answer accuracy | test | 1.0000 | small test set | `PROJECT_SUMMARY.json` |

### Behavioural checks
| capability | pass rate | known failure |
|---|---:|---|
| L2-normalised retrieval pipeline | PASS | Small corpus |
| Validation-only threshold selection | PASS | Threshold may not generalise |
| Cross-lingual retrieval | PASS in course workflow | Limited language/domain coverage |
| Re-ranking comparison | improvement +0.0556 MRR@3 | CPU latency is runtime-dependent |

### Limitations and risks
1. Corpus and query set are small.
2. Re-ranking latency is CPU/runtime dependent.
3. Threshold and retrieval quality are not validated for production distributions.

### Ethical and privacy notes
- Educational dataset only.
- Do not index confidential or sensitive personal data without additional safeguards.
- No production-search claim is made.

### Reproduction
1. افتح notebook: `bayan_NLP_ANAS_AI_Mutairi.ipynb`.
2. استخدم Google Colab / CPU.
3. ثبت النسخ من `requirements.txt`.
4. شغّل semantic-search and re-ranking cells بالترتيب.
5. قارن النتائج مع:
   - `reports/observed_search_manifest.json`
   - `reports/observed_reranking_display.json`
   - `PROJECT_SUMMARY.json`

---

## Overall limitations

1. المشروع يعتمد على بيانات تعليمية صغيرة وcourse fixtures.
2. النتائج المقاسة لا تمثل جودة إنتاجية أو تعميماً على بيانات حقيقية واسعة.
3. يجب إعادة التقييم عند تغيير البيانات، preprocessing، checkpoint، threshold، أو بيئة التشغيل.

## Overall ethical and privacy statement

This project is for educational and experimental use. It uses protected preprocessing and PII masking rules, does not claim production readiness, and requires human review before any real-world or high-impact use.
"""
p = Path("/mnt/data/MODEL_CARD.md")
p.write_text(text, encoding="utf-8")
print("created", p, p.stat().st_size)
