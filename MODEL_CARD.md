# بطاقة نموذج بيان | Bayan Model Card

**Student:** Anas Ibrahim Al-Mutairi  
**GitHub:** `Ans212121`  
**Program:** SDA-AIE-211 — Applied Natural Language Processing  
**Project:** Bayan

This card separates preserved evidence from work that still requires a clean correction run. No score is inferred when evidence has not yet been generated.

## 1. Topic classification

### Model details
- Name/version: Bayan Topic Classifier
- Base checkpoint: `distilbert/distilbert-base-multilingual-cased`
- Task: topic classification
- Result type: `MEASURED_SMOKE`
- Evidence: `reports/observed_classification.json`

### Data and preprocessing
- Languages: Arabic + English
- Split: 24 train / 8 validation / 8 test
- Group overlap: 0
- PII policy: mask course email/mobile patterns while preserving a separate display copy
- Tokenizer: checkpoint-matched multilingual tokenizer

### Evaluation

| metric | n | result | limitation |
|---|---:|---:|---|
| baseline validation Macro-F1 | 8 | 0.6667 | small set |
| Transformer validation Macro-F1 | 8 | 1.0000 | small set |
| baseline test Macro-F1 | 8 | 0.7333 | small set |
| Transformer test Macro-F1 | 8 | 0.8667 | small set |
| Transformer test accuracy | 8 | 0.8750 | small set |

### Intended use
Educational bilingual topic-classification experiments. Not for production/high-impact decisions.

---

## 2. Sentiment classification

### Model details
- Name/version: Bayan Sentiment Classifier
- Task: sentiment classification with its own label contract
- Status: **PENDING_CLEAN_RUN**
- Planned evidence: `reports/observed_sentiment.json`

The prior evaluated version did not preserve a separate sentiment metric. The corrected Notebook 03 now contains:
- a separate sentiment target;
- TF-IDF baseline;
- separate Transformer sequence-classification head;
- independent Macro-F1 export.

No sentiment score is claimed before the clean Colab run.

---

## 3. Named Entity Recognition

### Model details
- Name/version: Bayan NER
- Task: NER with BIO/subword alignment
- Result type: `MEASURED_SMOKE`
- Evidence: `reports/observed_ner_qa.json`

| metric | result |
|---|---:|
| Precision | 0.6667 |
| Recall | 0.5000 |
| strict entity F1 | 0.5714 |
| true entities | 4 |
| predicted entities | 3 |

Limit: very small entity count; this is not a production estimate.

---

## 4. Extractive QA

### Model details
- Name/version: Bayan Extractive QA
- Task: extractive answer span + no-answer handling
- Evidence: `reports/observed_ner_qa.json`

Preserved checks:
- token-offset/span alignment: PASS
- example span answer: `الرياض`
- no-answer handling: PASS
- short smoke training loss: 3.645052

Limit: course fixture and short smoke run; no broad EM/F1 claim is made.

---

## 5. Arabic preprocessing profile

- Profile: `search/1.0.0`
- Backend: `camel-tools==1.6.0`
- Evidence: `reports/observed_arabic_profile.json`
- Golden cases: **4/4 PASS**

Rules:
- preserve display copy;
- mask course PII patterns;
- Unicode normalisation without compatibility folding;
- remove Tatweel and diacritics;
- fold Alef/Alef Maksura;
- preserve Teh Marbuta.

Tiny Gulf fixture comparison:
- multilingual DistilBERT: Macro-F1 0.0000
- CAMeLBERT-DA: Macro-F1 0.6667

These are four-example `MEASURED_SMOKE` values only.

---

## 6. Semantic embeddings and core re-ranking

### Model details
- Embedding checkpoint: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Re-ranker: `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`
- Dimension: 384
- Normalisation: L2
- Index: FAISS `IndexFlatIP`
- Vector count: 24
- Evidence:
  - `reports/observed_search_manifest.json`
  - `reports/observed_reranking_display.json`

| metric | result |
|---|---:|
| Recall@3 | 1.0000 |
| MRR@3 before re-ranking | 0.6667 |
| MRR@3 after re-ranking | 0.7222 |
| delta | +0.0556 |

Re-ranking is part of the **core search architecture** and is not claimed as the R7 extension.

---

## 7. PROJECT_ARTIFACT optimisation/service

Status: **PENDING_CLEAN_RUN**

The preserved Day 4 benchmark was `SYSTEMS_SMOKE`. Corrected Notebook 08 is prepared to use the saved Bayan topic checkpoint and its validation workload, then measure:
- PyTorch FP32;
- ONNX FP32;
- dynamic INT8;
- p50/p95/p99 and throughput;
- observed memory;
- task Macro-F1 and quality tax;
- FastAPI contract/canaries;
- explicit adopt/reject/rollback decision.

Planned evidence:
- `reports/benchmark_results.json`
- `reports/service_smoke.json`
- `BENCHMARKS.md`

---

## 8. Measured extension — batch endpoint

Status: **PENDING_CLEAN_RUN**

Chosen R7 extension: **batch endpoint**.

The corrected Notebook 08 will compare sequential single-item inference with a true batched model call, using the same examples and at least 30 measured repetitions after warm-up. It also checks prediction agreement so speed is not accepted at the cost of changed outputs.

Planned evidence: `reports/extension_batch_endpoint.json`.

---

## Overall limitations and ethics

- Small educational/course-fixture datasets.
- Limited Gulf dialect/Arabizi coverage.
- Several results are smoke evidence, not production estimates.
- Runtime measurements vary with Colab CPU conditions.
- Real personal/sensitive data must not be uploaded.
- Human review and stronger external validation are required before real-world/high-impact use.

## Reproduction

Run notebooks 00→08 from `notebooks/` in Google Colab, using the day-specific requirements files, then run the course validators described in `README.md`.
