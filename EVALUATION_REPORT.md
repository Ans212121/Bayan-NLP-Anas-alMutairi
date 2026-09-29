# تقرير تقييم بيان | Bayan Evaluation Report

## 1. نطاق التقرير

- تاريخ التشغيل: `2026-09-28`
- commit SHA: `يضاف عند إنشاء النسخة النهائية submission-v1.0`
- runtime/device: `Google Colab / CPU`
- data version/hash: `bayan_day3_cases.csv — SHA256: 7708cbe884a3c268d24ed2cb87ad2f0a8b64b2e6fa6b37a32393b6ae3bd50e5b`
- preprocessing profile/version/backend: `arabic-search/1.0.0 + english-nfc-whitespace/1.0.0`
- model/checkpoint IDs:
  - `distilbert/distilbert-base-multilingual-cased`
  - `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
  - `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`
- نوع الأرقام: `MEASURED_SMOKE`

## 2. العقود قبل القياس

| العقد | الدليل | الحالة |
|---|---|---|
| لا PII حقيقية | PII masking with `<EMAIL>` and `<PHONE>` in preprocessing | PASS |
| train/validation/test بلا leakage | grouped split isolation; group overlap = 0 | PASS |
| tokenizer/model متطابقان | DistilBERT tokenizer/model checkpoint used consistently | PASS |
| Arabic profile متطابقة في train/index/query/serve | `arabic-search/1.0.0 + english-nfc-whitespace/1.0.0` | PASS |
| corpus/query embeddings مطبعة L2 | semantic-search manifest: `normalization = l2` | PASS |
| frozen test لم يستخدم في tuning | threshold/model selection performed on validation only | PASS |

## 3. نتائج المهام

| المهمة | المقياس الرئيس | النتيجة | CI/تكرار | مجموعة القياس |
|---|---|---:|---|---|
| Classification | Macro-F1 | 0.8667 | one measured smoke run | test |
| NER | strict entity F1 | 0.5714 | 4 true entities / 3 predicted | test fixture |
| QA | span/no-answer validation | PASS | valid-span and no-answer tests | course fixture |
| Retrieval | Recall@3 / MRR@3 | 1.0000 / 0.7222 | 6 answerable test queries | test |

Additional classification result:
- Transformer test accuracy: **0.875**

Additional retrieval result:
- MRR@3 before re-ranking: **0.6667**
- MRR@3 after re-ranking: **0.7222**
- Improvement: **+0.0556**

## 4. شرائح التقييم

The notebook includes slice-based evaluation and explicitly flags small slices.

| المهمة | الشريحة | n | metric | 95% CI | التحذير/التفسير |
|---|---|---:|---:|---|---|
| Evaluation | `language=ar` | small | recorded in notebook slice report | reported in notebook | small-slice uncertainty |
| Evaluation | `language=en` | small | recorded in notebook slice report | reported in notebook | small-slice uncertainty |
| Evaluation | `variant=Gulf` | small | recorded in notebook slice report | reported in notebook | limited dialect coverage |
| Evaluation | `length=long` | small | recorded in notebook slice report | reported in notebook | limited sample size |

Detailed evidence is stored in:
- `day3_slice_report.csv`
- `reports/EVALUATION_REPORT.md`

## 5. مقارنة الإصدارات

- Model A: `baseline classifier`
- Model B: `distilbert/distilbert-base-multilingual-cased`
- observed difference B−A on validation Macro-F1: `+0.3333`
- baseline validation Macro-F1: `0.6667`
- Transformer validation Macro-F1: `1.0000`
- paired 95% CI: `see notebook paired comparison / evaluation evidence`
- القرار المهني: The Transformer improved the measured validation score in this small course fixture, but the sample is too small to claim production superiority.

## 6. Behavioural tests

| النوع | passed/total | pass rate | فشل مهم |
|---|---:|---:|---|
| invariance / directional / minimum functionality combined | 3 / 6 | 0.5000 | dialect gap, hard/ambiguous cases, class confusion |

Overall:
- Passed: **3 / 6**
- Pass rate: **0.5000**

## 7. تحليل الأخطاء

- المصدر: validation + behavioural failures only.
- عدد الأخطاء المقروءة يدويًا: documented in the notebook error-analysis workflow
- رابط worksheet داخل المستودع: `day3_error_taxonomy.csv`

| taxonomy tag | count | مثال آمن مختصر | الفرضية |
|---|---:|---|---|
| dialect gap | documented in worksheet | Gulf/Arabic wording variation | limited dialect coverage |
| hard/ambiguous cases | documented in worksheet | ambiguous class wording | overlapping semantic cues |
| class confusion | documented in worksheet | similar topic labels | insufficient separation between classes |

## 8. الإصلاحات الثلاثة ذات الأولوية

| الأولوية | الدليل | الإجراء | metric/slice المتوقع | الكلفة | اختبار عدم الرجوع |
|---:|---|---|---|---|---|
| 1 | dialect-gap errors | expand Gulf-dialect examples | Arabic/Gulf slice | medium | rerun slice metrics |
| 2 | class-confusion errors | add harder contrastive examples | classification Macro-F1 | medium | compare frozen test |
| 3 | ambiguous cases | review labels and boundary cases | behavioural pass rate | low/medium | rerun behavioural tests |

## 9. ما الذي لا تثبته النتائج؟

The results do not prove production readiness or broad generalisation.

Main limitations:
- small educational datasets
- synthetic/course-fixture examples
- small validation and test sets
- CPU runtime-dependent latency
- limited Arabic dialect and Arabizi coverage
- limited NER entity counts
- short smoke-test training runs
- no production traffic or real-world deployment evaluation

## 10. خلاصة للإدارة

The Bayan project successfully demonstrates an end-to-end applied NLP workflow across classification, NER, QA, bilingual semantic search, evaluation, and optimisation. The strongest measured results include classification test Macro-F1 of **0.8667**, semantic-search Recall@3 of **1.0000**, and re-ranking improvement from MRR@3 **0.6667** to **0.7222**.

The main weaknesses are the small course datasets, behavioural pass rate of **0.5000**, limited dialect coverage, and uncertainty in small evaluation slices. The next recommended step is to improve Gulf-dialect coverage, reduce class-confusion errors, and rerun the frozen evaluation before making any production-quality claim.
