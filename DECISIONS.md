# DECISIONS — Bayan

This file records project decisions that are supported by the student's saved run in `bayan_NLP_ANAS_AI_Mutairi (2).ipynb` and by evidence under `reports/`.

## D-001 — Tokenizer and maximum length

- **Gate:** A — ingest
- **Status:** accepted for the course workflow
- **Owner:** Anas Ibrahim Al-Mutairi
- **Evidence:** `reports/observed_classification.json` and the saved Day 1 outputs in the student notebook

### Evidence from the saved run

- Local WordPiece token fertility by sample: **[1.17, 1.00, 1.50, 2.00, 1.14]**
- Mean token fertility: **1.36**
- Truncation rate at length 10 on the Day 1 sample: **0%**
- The local demonstration tokenizer produced `[UNK]` tokens on Arabic examples.
- The multilingual Hugging Face tokenizer was a fast tokenizer and produced meaningful Arabic subwords.

### Decision

Use the checkpoint-matched multilingual tokenizer for Transformer tasks rather than the small local WordPiece demonstration vocabulary. Keep task-specific maximum lengths explicit in each notebook and audit truncation instead of assuming it is safe.

### Rejected alternative

The local WordPiece tokenizer was retained only as a teaching demonstration because its tiny vocabulary produced `[UNK]` tokens on Arabic text and is not suitable as the project model tokenizer.

## D-002 — Arabic preprocessing profile and CAMeL Tools

- **Gate:** C — search & truth
- **Status:** accepted
- **Evidence:** `reports/observed_arabic_profile.json`

Selected profile: **search/1.0.0**, backend **camel-tools==1.6.0**.

Rules:
- preserve a separate display/raw copy;
- mask the course PII patterns;
- Unicode normalisation without compatibility folding;
- remove Tatweel and diacritics for the search copy;
- fold Alef variants and Alef Maksura;
- preserve Teh Marbuta.

Golden tests: **4/4 PASS**.

A small course-fixture comparison also recorded Gulf-test Macro-F1 **0.0000** for multilingual DistilBERT and **0.6667** for CAMeLBERT-DA on only four examples. Because the slice is extremely small, this is recorded as `MEASURED_SMOKE`, not a broad superiority claim.

## D-003 — Attention interpretation boundary

- **Gate:** A / architecture
- **Status:** accepted

Scaled dot-product attention, masking, multi-head reshaping and NumPy↔PyTorch parity are validated in Notebook 02. Attention weights are treated as **descriptive internal weights, not causal proof of why a model made a decision**. A heatmap can show where attention mass is placed, but it does not by itself establish feature importance or causality.

## D-004 — Topic-classification model and split

- **Gate:** B — tasks
- **Status:** accepted for measured smoke evidence
- **Evidence:** `reports/observed_classification.json`

Grouped split: train **24**, validation **8**, test **8**, group overlap **0**.

- TF-IDF baseline validation Macro-F1: **0.6667**
- Transformer validation Macro-F1: **1.0000**
- TF-IDF baseline test Macro-F1: **0.7333**
- Transformer test Macro-F1: **0.8667**
- Transformer test accuracy: **0.875**
- selected epoch: **9**

The Transformer is used for the project topic path, with the explicit limitation that this is a small educational run.

## D-005 — Sentiment head is a separate task

- **Gate:** B — tasks
- **Status:** prepared; clean rerun required

The grading feedback correctly identified that topic metrics cannot be reused as sentiment evidence. The corrected Notebook 03 contains a **separate sentiment label contract, TF-IDF baseline and separate Transformer sequence-classification head** and writes `reports/observed_sentiment.json`.

No sentiment Macro-F1 is claimed in this file until the corrected notebook is run and its saved output is committed.

## D-006 — Semantic retrieval and threshold

- **Gate:** C — search & truth
- **Status:** accepted for measured smoke evidence
- **Evidence:** `reports/observed_search_manifest.json`, `reports/observed_reranking_display.json`

- embedding model: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- dimension: **384**
- L2 normalisation: enabled
- index: **FAISS IndexFlatIP**
- vector count: **24**
- threshold selected on validation only: **0.4592095613**
- Recall@3: **1.0000**
- MRR@3 before re-ranking: **0.6667**
- MRR@3 after re-ranking: **0.7222**

Cross-encoder re-ranking is documented as part of the **core search requirement**, not as the R7 extension.

## D-007 — Evaluation, slices and error priorities

- **Gate:** C — search & truth
- **Status:** accepted
- **Evidence:** `reports/day3_evaluation_fixture.json`, `reports/day3_slice_report.csv`, `reports/day3_error_taxonomy.csv`

Paired fixture difference B−A: **0.00120**, 95% bootstrap CI **[-0.10472, 0.09963]**. Because the interval includes zero, the evidence does **not** support a directional superiority claim.

Manual taxonomy counts:
- `dialect_gap`: **3**
- `hard_or_ambiguous`: **3**
- `class_confusion`: **2**

Priorities are therefore:
1. improve Gulf health/transport coverage;
2. add contrastive examples for app/status class confusion;
3. handle underspecified short requests with more context or abstention.

## D-008 — Day 4 benchmark and ship decision

- **Gate:** D — ship
- **Status:** clean project-artifact rerun required

The preserved run is only **SYSTEMS_SMOKE**. Its ONNX/INT8 latency and parity values are useful for validating mechanics, but they are **not a final project ship decision**.

The corrected Notebook 08 is configured to load the saved Bayan topic model and validation workload as `PROJECT_ARTIFACT`, measure p50/p95/p99, throughput, observed memory and task-quality tax, then make an ADOPT/REJECT/KEEP-FP32 decision with an FP32 rollback path.

No PROJECT_ARTIFACT result is claimed until that clean run finishes.

## D-009 — Required measured extension

- **Gate:** R7 / D
- **Status:** prepared; clean rerun required
- **Chosen extension:** **batch endpoint**
- **Planned evidence:** `reports/extension_batch_endpoint.json`

Re-ranking was removed as the claimed extension because it is part of the core semantic-search requirement. The corrected Notebook 08 measures a true batch inference endpoint against sequential single-item calls on the same examples, checks prediction agreement, records throughput/latency benefit and cost, and writes an ADOPT/REJECT decision.

## Gate-E checklist

- [x] tokenizer + maximum-length decision documented
- [x] Arabic preprocessing profile documented
- [x] topic model/baseline/split documented
- [x] semantic encoder/index/threshold documented
- [x] evaluation slices/error priorities documented
- [x] attention interpretation limitation documented
- [ ] separate sentiment clean-run evidence committed
- [ ] PROJECT_ARTIFACT benchmark completed
- [ ] ONNX/INT8 project decision completed
- [ ] batch-endpoint measured extension completed
- [ ] final validator/preflight reports committed
