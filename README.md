# Bayan — Bilingual Applied NLP Project

**Learner / المتدرب:** Anas Ibrahim Al-Mutairi  
**GitHub:** `Ans212121`  
**Program:** Applied Natural Language Processing with Transformers  
**Program code:** `SDA-AIE-211`  
**Trainer:** Meaad Al-Marri — ميعاد المري

## Executive summary | الملخص

Bayan is an educational bilingual NLP system for Arabic and English feedback. The project covers privacy-aware preprocessing, topic and sentiment classification, NER, extractive QA with no-answer handling, bilingual semantic search, evaluation/error analysis, optimisation and a tested service interface.

The preserved results in this repository come from the student's own Colab run and are labelled honestly as `MEASURED_SMOKE` or `COURSE_FIXTURE`. They are not production claims. A correction cycle is in progress to add the missing separate sentiment evidence, rerun Day 4 on the actual project artefact, and measure a valid R7 extension.

## Problem, scope and non-goals

**Problem.** Convert Arabic/English feedback into a documented NLP response while preserving privacy and producing evidence that can be reproduced.

**In scope.**
- protected preprocessing and PII masking;
- topic and sentiment classification as separate label contracts;
- Named Entity Recognition;
- extractive QA and no-answer logic;
- multilingual embeddings + FAISS + core re-ranking;
- sliced evaluation, confidence intervals and manual error taxonomy;
- PROJECT_ARTIFACT performance benchmarking and service tests;
- one additional measured extension.

**Out of scope.**
- production government deployment;
- decisions about real individuals;
- unreviewed use on sensitive/private data;
- treating smoke/course-fixture results as production estimates.

## Architecture | المعمارية

```mermaid
flowchart TD
    A["AR/EN feedback"] --> B["Raw/display copy + PII masking"]
    B --> C["Versioned preprocessing profile"]
    C --> D["Checkpoint-matched tokenizer"]
    D --> E["Transformer embeddings"]
    E --> F["Transformer encoder blocks"]
    F --> G1["Topic head"]
    F --> G2["Separate sentiment head"]
    F --> G3["NER head"]
    F --> G4["Extractive QA head + no-answer"]
    C --> H["Sentence embedding"]
    H --> I["L2 normalisation + FAISS IndexFlatIP"]
    I --> J["Cross-encoder re-ranking (core search)"]
    G1 --> K["Unified evidence / service"]
    G2 --> K
    G3 --> K
    G4 --> K
    J --> K
    K --> L["Evaluation + API + benchmark"]
```

### Encoder flow

For Transformer tasks, text first passes through the project preprocessing contract, then the tokenizer produces input IDs and attention masks. The embedding layer maps token IDs to vectors. Those vectors pass through stacked Transformer encoder blocks, where self-attention and feed-forward layers update contextual token representations. A task-specific head then consumes the resulting representation: sequence-classification heads for topic/sentiment, token-level outputs for NER, or start/end span scores for extractive QA.

### Attention interpretation boundary

The project validates scaled dot-product attention, masking, multi-head reshaping and NumPy↔PyTorch parity. **Attention weights are descriptive internal weights and are not causal proof of why a prediction was made.** An attention map can show where attention mass was placed, but it does not by itself establish feature importance or causality.

## Reproduce on Google Colab Free

Open the notebooks from **this repository**, save your own copy in Drive, then use **Runtime → Restart session and run all**. The corrected notebooks are derived from the student's actual project work rather than the trainer starter outputs.

| # | Notebook | Open in Colab | Purpose |
|---:|---|---|---|
| 00 | [runtime doctor](notebooks/00_runtime_doctor.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/00_runtime_doctor.ipynb) | environment |
| 01 | [text processing/tokenisation](notebooks/01_text_processing_tokenization.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/01_text_processing_tokenization.ipynb) | Gate A |
| 02 | [attention/transformers](notebooks/02_attention_transformers.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/02_attention_transformers.ipynb) | architecture |
| 03 | [topic + separate sentiment](notebooks/03_text_classification.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/03_text_classification.ipynb) | Gate B |
| 04 | [NER and QA](notebooks/04_ner_and_qa.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/04_ner_and_qa.ipynb) | Gate B |
| 05 | [Arabic NLP](notebooks/05_arabic_nlp.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/05_arabic_nlp.ipynb) | Gate C |
| 06 | [semantic search](notebooks/06_semantic_search.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/06_semantic_search.ipynb) | Gate C |
| 07 | [evaluation/error analysis](notebooks/07_evaluation_error_analysis.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/07_evaluation_error_analysis.ipynb) | Gate C |
| 08 | [optimisation/serving + batch extension](notebooks/08_optimization_serving.ipynb) | [Colab](https://colab.research.google.com/github/Ans212121/Bayan-NLP-Anas-alMutairi/blob/main/notebooks/08_optimization_serving.ipynb) | Gate D / R7 |

Dependencies are pinned by day:
- [requirements-day1.txt](requirements-day1.txt)
- [requirements-day2.txt](requirements-day2.txt)
- [requirements-day3.txt](requirements-day3.txt)
- [requirements-day4.txt](requirements-day4.txt)

## Preserved measured evidence

| Component | Metric | Result + label | Evidence |
|---|---|---:|---|
| topic baseline | test Macro-F1 | **0.7333 — MEASURED_SMOKE** | [observed_classification.json](reports/observed_classification.json) |
| topic Transformer | test Macro-F1 | **0.8667 — MEASURED_SMOKE** | [observed_classification.json](reports/observed_classification.json) |
| topic Transformer | test accuracy | **0.8750 — MEASURED_SMOKE** | [observed_classification.json](reports/observed_classification.json) |
| sentiment | Macro-F1 | **PENDING_CLEAN_RUN** | corrected Notebook 03 will write `reports/observed_sentiment.json` |
| NER | strict entity F1 | **0.5714 — MEASURED_SMOKE** | [observed_ner_qa.json](reports/observed_ner_qa.json) |
| QA | span + no-answer checks | **PASS — COURSE_FIXTURE** | [observed_ner_qa.json](reports/observed_ner_qa.json) |
| search | Recall@3 | **1.0000 — MEASURED_SMOKE** | [search manifest](reports/observed_search_manifest.json) + saved notebook |
| core re-ranking | MRR@3 | **0.6667 → 0.7222** | [observed_reranking_display.json](reports/observed_reranking_display.json) |
| behaviour suite | pass rate | **3/6 = 0.5000 — COURSE_FIXTURE** | [day3_evaluation_fixture.json](reports/day3_evaluation_fixture.json) |

Exact slices and error evidence:
- [day3_slice_report.csv](reports/day3_slice_report.csv)
- [day3_error_taxonomy.csv](reports/day3_error_taxonomy.csv)
- [day3_evaluation_fixture.json](reports/day3_evaluation_fixture.json)

## Error found and decision

Manual error review identified:
- `dialect_gap`: **3**
- `hard_or_ambiguous`: **3**
- `class_confusion`: **2**

The weakest recorded fixture slice was `length=long` with Macro-F1 **0.5259**, 95% CI **[0.3918, 0.8308]**. The paired A/B comparison had B−A **+0.0012**, 95% CI **[-0.1047, 0.0996]**, so the fixture does not support a directional superiority claim.

Priority fixes are documented in [EVALUATION_REPORT.md](EVALUATION_REPORT.md) and [DECISIONS.md](DECISIONS.md).

## Day 4 claim boundary

The old Day 4 result is explicitly **SYSTEMS_SMOKE**. It is not the final project benchmark.

Corrected Notebook 08 is prepared to:
1. load the saved Bayan topic model and validation workload;
2. measure PyTorch / ONNX FP32 / dynamic INT8 on the same project examples;
3. record p50/p95/p99, throughput, memory and Macro-F1 quality tax;
4. make an evidence-based ship/rollback decision;
5. write `reports/benchmark_results.json`.

See [BENCHMARKS.md](BENCHMARKS.md).

## Required measured extension

The project now uses **batch endpoint** as the R7 extension. Cross-encoder re-ranking is kept as a core search component and is no longer claimed as the extension.

Corrected Notebook 08 compares sequential single-item calls with a true batch call, checks prediction agreement, and measures latency/throughput trade-off. It will write `reports/extension_batch_endpoint.json` after the clean run.

## Repository structure

```text
.
├── README.md
├── STUDENT_PROFILE.md
├── PROGRESS.md
├── DECISIONS.md
├── BENCHMARKS.md
├── EVALUATION_REPORT.md
├── MODEL_CARD.md
├── DATA_CARD.md
├── PROJECT_SUMMARY.json
├── SUBMISSION.yml
├── PRESENTATION.md
├── notebooks/
│   ├── 00_runtime_doctor.ipynb
│   ├── 01_text_processing_tokenization.ipynb
│   ├── 02_attention_transformers.ipynb
│   ├── 03_text_classification.ipynb
│   ├── 04_ner_and_qa.ipynb
│   ├── 05_arabic_nlp.ipynb
│   ├── 06_semantic_search.ipynb
│   ├── 07_evaluation_error_analysis.ipynb
│   └── 08_optimization_serving.ipynb
├── src/bayan/
├── tests/
├── reports/
├── sample_outputs/
└── requirements-day1.txt ... requirements-day4.txt
```

The root file `bayan_NLP_ANAS_AI_Mutairi (2).ipynb` is retained as provenance for the student's earlier combined Colab run. Final grading evidence should come from the corrected official 00–08 paths after their clean run.

## Final validation workflow

After all nine notebooks are clean-run and saved with outputs:

```bash
PYTHONPATH=src python -m pytest -q tests
PYTHONPATH=src python scripts/validate_submission.py . --json-report reports/submission_validation.json
PYTHONPATH=src python scripts/preflight_submission.py . --report reports/preflight.json
```

After the corrected final tag is created according to the trainer's resubmission instructions:

```bash
PYTHONPATH=src python scripts/validate_submission.py . --require-tag
PYTHONPATH=src python scripts/preflight_submission.py . --require-tag --report reports/preflight.json
```

## Limitations and responsible use

- Course datasets and many slices are small.
- Smoke and course-fixture metrics are not production estimates.
- Gulf dialect and Arabizi coverage is limited.
- NER evidence contains very few entities.
- Runtime latency varies with Colab CPU conditions.
- Real sensitive data must not be added.
- Any real-world/high-impact use requires stronger validation and human review.

## My contribution | مساهمتي

I built and ran the student project workflow in my own combined Colab notebook, including:
- the two-copy preprocessing contract and PII masking;
- local WordPiece metrics and checkpoint-matched multilingual tokenisation;
- attention/masking/multi-head/parity experiments;
- grouped topic-classification baseline and Transformer fine-tuning;
- NER BIO/subword alignment and extractive QA/no-answer handling;
- Arabic preprocessing profiles and CAMeL Tools checks;
- bilingual sentence embeddings, L2 normalisation, FAISS retrieval and re-ranking;
- bootstrap confidence intervals, slice analysis and manual error taxonomy.

For the correction cycle, my project notebooks were reorganised into the required 00–08 paths, a **separate sentiment head** was added, and a **batch endpoint** extension plus a true PROJECT_ARTIFACT Day 4 rerun were prepared. New measured values are not claimed until I run and inspect them.

## AI assistance | الاستعانة بالأدوات

I used **ChatGPT by OpenAI** as an assistance tool to:
- interpret the grading feedback and course requirements;
- reorganise my own notebook work into the required repository structure;
- review documentation links and evidence paths;
- suggest/debug code for the separate sentiment task, PROJECT_ARTIFACT benchmark setup and batch-endpoint extension.

I verify this assistance by reading the code, running the notebooks myself in Google Colab, checking saved outputs and Core markers, running the course tests/validators, and comparing documentation claims against generated evidence files. Course materials, libraries, models and datasets remain attributed to their original sources.

## Training context | السياق التدريبي

This educational project was developed during Applied Natural Language Processing
with Transformers (SDA-AIE-211) in the SDAIA Academy training context.

أُنجز هذا المشروع التعليمي ضمن دورة معالجة اللغات الطبيعية باستخدام المحولات
(SDA-AIE-211) في السياق التدريبي لأكاديمية سدايا.

Academy | الأكاديمية: [SDAIA Academy](https://github.com/SDAIAAcademy)  
Trainer | المدربة: Meaad Al-Marri — ميعاد المري  
Course source | مصدر الدورة: https://github.com/almiyead-rgb/bayan-applied-nlp-course  
#SDAIAAcademy

This attribution does not claim Academy endorsement or ownership of third-party assets.

## Correction status

A backup of the repository before this correction cycle is preserved in branch:

`backup-before-2026-09-30-evaluation-fixes`

The old `submission-v1.0` release corresponds to the previously assessed version. The corrected release must only be finalised after clean notebook runs, validators and the trainer's allowed resubmission procedure.
