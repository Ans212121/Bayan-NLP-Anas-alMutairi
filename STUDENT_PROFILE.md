# STUDENT PROFILE | ملف المتدرب

- Display name | الاسم للعرض: Anas Ibrahim Al-Mutairi
- GitHub username: Ans212121
- Public repository: https://github.com/Ans212121/Bayan-NLP-Anas-alMutairi
- Learning lane completed: Core correction cycle in progress
- Starting level (self-described): beginner

## My contribution | مساهمتي

This is an individual educational project. My actual Colab work implemented the preprocessing/tokenisation, attention experiments, grouped topic classification, NER, extractive QA, Arabic profiles, multilingual semantic search and evaluation/error-analysis workflow.

Concrete examples of my work include:
- Day 1 preprocessing/token metrics: mean fertility **1.36**, 0% truncation on the length-10 lab sample and PII masking checks.
- Topic classification: grouped 24/8/8 split with zero group overlap and Transformer test Macro-F1 **0.8667**.
- Arabic profile: `search/1.0.0` with CAMeL Tools and **4/4** golden cases passing.
- Search/evaluation: L2 + FAISS retrieval, validation-only thresholding, slice confidence intervals and an eight-example manual error taxonomy.

For the correction cycle I reorganised my actual work into the required nine notebook paths. I also added a separate sentiment head and prepared a PROJECT_ARTIFACT Day 4 rerun plus a measured batch-endpoint extension. I will only claim their new metrics after I run and inspect them in Colab.

## AI/tool assistance disclosure | الإفصاح عن المساعدة

I used **ChatGPT by OpenAI** to help interpret the assessment feedback, reorganise my existing project code/documentation, check repository paths, and suggest/debug the correction code for the sentiment head, project benchmark configuration and batch endpoint.

I verify the assistance by reading the code, running the notebooks myself, checking saved outputs/Core markers, running the course tests and validators, and comparing every documented number with a generated evidence file. The final submitted results are not accepted merely because an AI tool suggested them.

## One skill I can now demonstrate

I can build and evaluate a bilingual semantic-search pipeline using multilingual sentence embeddings, L2 normalisation, FAISS `IndexFlatIP`, validation-only thresholding and core cross-encoder re-ranking.

Evidence:
- `notebooks/06_semantic_search.ipynb`
- `reports/observed_search_manifest.json`
- `reports/observed_reranking_display.json`
- `EVALUATION_REPORT.md`

## One limitation I understand

Strong scores on small educational datasets do not prove production readiness or broad generalisation. Small slices, limited dialect coverage, ambiguous labels and runtime variability can materially change the results. Real-world use would require larger representative data, privacy/security review, independent evaluation and human oversight.

## Integrity declaration | إقرار النزاهة

- [x] أفهم كل كود وقرار أسلمه ويمكنني شرحه.
- [x] نسبت المصادر والمكتبات والنماذج والبيانات إلى أصحابها.
- [x] لم أستخدم بيانات شخصية أو أسرارًا.
- [x] لم أغيّر test labels أو validator للحصول على PASS.

Signature/display name: Anas Ibrahim Al-Mutairi  
Correction date: 2026-09-30
