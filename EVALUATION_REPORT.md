# تقرير تقييم بيان | Bayan Evaluation Report

## 1. نطاق التقرير

- تاريخ التشغيل المحفوظ: **2026-09-29**
- Commit الذي كان يحتوي التشغيل الفعلي الذي قيّمته المدربة: `e6a4f3e0ba8478464ae8c24bd29f09df1d6c0026`
- Runtime/device: **Google Colab / CPU**
- Data version/hash: `bayan_day3_cases.csv` — SHA256 `7708cbe884a3c268d24ed2cb87ad2f0a8b64b2e6fa6b37a32393b6ae3bd50e5b`
- Arabic preprocessing: `search/1.0.0`, backend `camel-tools==1.6.0`
- Search preprocessing: `arabic-search/1.0.0 + english-nfc-whitespace/1.0.0`
- Main checkpoints:
  - `distilbert/distilbert-base-multilingual-cased`
  - `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
  - `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`
- Current preserved result labels: **MEASURED_SMOKE / COURSE_FIXTURE**

A corrected clean run is still required for the separate sentiment head and the Day 4 PROJECT_ARTIFACT benchmark.

## 2. العقود قبل القياس

| العقد | الدليل | الحالة |
|---|---|---|
| لا PII حقيقية | raw/model two-copy preprocessing + `<EMAIL>` / `<PHONE>` masking | PASS |
| train/validation/test بلا leakage | grouped classification split; overlap = 0 | PASS |
| tokenizer/model متطابقان | model-matched multilingual tokenizer | PASS |
| Arabic profile موثقة | `reports/observed_arabic_profile.json` | PASS |
| corpus/query embeddings مطبعة L2 | `reports/observed_search_manifest.json` | PASS |
| threshold لم يُضبط على test | validation-only threshold selection | PASS |

## 3. نتائج المهام المحفوظة

| المهمة | المقياس الرئيس | النتيجة | النطاق | الدليل |
|---|---|---:|---|---|
| Topic classification | test Macro-F1 | **0.8667** | 8 test rows, MEASURED_SMOKE | `reports/observed_classification.json` |
| Topic baseline | test Macro-F1 | **0.7333** | 8 test rows | `reports/observed_classification.json` |
| Topic classification | test accuracy | **0.8750** | 8 test rows | `reports/observed_classification.json` |
| Sentiment | Macro-F1 | **PENDING_CLEAN_RUN** | separate head added to corrected Notebook 03 | `reports/observed_sentiment.json` after run |
| NER | strict entity F1 | **0.5714** | 4 true / 3 predicted entities | `reports/observed_ner_qa.json` |
| QA | valid-span / no-answer | **PASS / PASS** | course fixture | `reports/observed_ner_qa.json` |
| Retrieval | Recall@3 | **1.0000** | small course test set | `reports/observed_search_manifest.json` + saved notebook |
| Re-ranking | MRR@3 | **0.6667 → 0.7222** | 6 answerable queries | `reports/observed_reranking_display.json` |

## 4. شرائح التقييم — COURSE_FIXTURE

These rows come from the 36-row evaluation fixture. They test the evaluation method and must not be presented as production estimates.

| الشريحة | n | Macro-F1 | 95% bootstrap CI | ملاحظة |
|---|---:|---:|---|---|
| ALL | 36 | **0.7819** | **[0.6112, 0.8962]** | course fixture |
| language=ar | 24 | **0.7583** | **[0.5607, 0.9265]** | wide uncertainty |
| language=en | 12 | **0.8286** | **[0.5000, 1.0000]** | SMALL_SLICE |
| variant=English | 12 | **0.8286** | **[0.4965, 1.0000]** | SMALL_SLICE |
| variant=Gulf | 12 | **0.6583** | **[0.2941, 0.8952]** | SMALL_SLICE |
| variant=MSA | 12 | **0.8375** | **[0.5304, 1.0000]** | SMALL_SLICE |
| length=long | 18 | **0.5259** | **[0.3918, 0.8308]** | weak long-text slice |
| length=short | 18 | **0.8286** | **[0.6250, 1.0000]** | course fixture |

Exact CSV: `reports/day3_slice_report.csv`.

## 5. مقارنة مزدوجة

On the same 36 paired fixture rows:

- Model A Macro-F1: **0.7807469**, 95% CI **[0.6212498, 0.8982313]**
- Model B Macro-F1: **0.7819444**, 95% CI **[0.6169213, 0.9042123]**
- Observed B−A: **+0.0011975**
- Paired 95% CI: **[-0.1047232, 0.0996301]**
- Directional superiority supported: **No**

**Interpretation:** the interval includes zero, so this fixture does not support a claim that B is directionally better than A.

Evidence: `reports/day3_evaluation_fixture.json`.

## 6. Behavioural tests

Six explicit course-fixture behavioural cases were inspected.

- Passed: **3 / 6**
- Pass rate: **0.5000**
- Failures:
  - `EV-006`: expected health, predicted transport
  - `EV-030`: expected health, predicted transport
  - `EV-020`: expected transport, predicted digital_service

## 7. تحليل الأخطاء اليدوي

Eight failing/misclassified examples were tagged manually in the notebook.

| taxonomy tag | count | أمثلة | الفرضية |
|---|---:|---|---|
| dialect_gap | **3** | EV-006, EV-010, EV-012 | Gulf/colloquial phrasing is under-covered |
| hard_or_ambiguous | **3** | EV-007, EV-030, EV-031 | the request omits a decisive task cue |
| class_confusion | **2** | EV-019, EV-020 | app/status words overlap multiple topics |

Worksheet: `reports/day3_error_taxonomy.csv`.

## 8. الإصلاحات الثلاثة ذات الأولوية

| الأولوية | الدليل | الإجراء | قياس القبول |
|---:|---|---|---|
| 1 | dialect_gap = 3 | collect/review targeted Gulf health + transport examples | rerun Gulf slice + behavioural cases |
| 2 | EV-019 / EV-020 class confusion | add contrastive app/status examples and review label guide | paired comparison with no regression |
| 3 | ambiguous/underspecified = 3 | request context or abstain at low confidence | ambiguity behavioural suite |

## 9. حدود النتائج

The saved results do not establish production readiness. The datasets and slices are small, several values are course fixtures or smoke measurements, dialect coverage is limited, NER has very few entities, and latency depends on the Colab CPU/runtime.

The preserved Day 4 measurements are **SYSTEMS_SMOKE only** and are not a final project benchmark.

## 10. خلاصة

The preserved run demonstrates an end-to-end bilingual NLP workflow and provides traceable topic, NER, QA, retrieval and evaluation evidence. Topic test Macro-F1 is **0.8667**, NER F1 is **0.5714**, and retrieval re-ranking changes MRR@3 from **0.6667** to **0.7222** on six answerable course queries.

The corrected project now separates sentiment from topic classification, prepares a real PROJECT_ARTIFACT Day 4 rerun, and replaces re-ranking as the claimed R7 extension with a measured **batch endpoint**. Those new values must come from a clean Colab run before final submission.
