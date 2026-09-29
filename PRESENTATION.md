# PRESENTATION — Bayan | عرض بيان

**GitHub username / معرف المتدرب:** Ans212121

## 1. Problem and user | المشكلة والمستخدم

Bayan is an educational Applied NLP project for Arabic and English text.

- **User:** student/trainer evaluating the Bayan NLP workflow.
- **Input:** Arabic or English text, depending on the task.
- **Scope:** text preprocessing, classification, NER, extractive QA, semantic search, evaluation, and optimisation.
- **Non-goals:** production deployment, high-impact decision making, or processing sensitive personal data without additional safeguards.

## 2. Architecture | المعمارية

Architecture reference: `README.md`

Main data flow:

`Raw text → protected preprocessing → tokenisation/embeddings → task model → evaluation → evidence/report`

For semantic search:

`Query → Arabic/English preprocessing → multilingual embedding → L2 normalisation → FAISS retrieval → cross-encoder re-ranking → threshold/no-answer decision`

Main evidence files:
- `README.md`
- `MODEL_CARD.md`
- `DATA_CARD.md`
- `EVALUATION_REPORT.md`
- `BENCHMARKS.md`
- `DECISIONS.md`

## 3. Demonstration | التطبيق

- **Arabic example + output evidence:**  
  QA example extracted the answer `الرياض`.  
  Evidence: `reports/observed_ner_qa.json`

- **English example + output evidence:**  
  English requests were successfully handled in the tested service workflow.  
  Evidence: `BENCHMARKS.md` — English inference `200` and English canary `PASS`

- **No-answer / invalid-input case:**  
  QA no-answer handling returned `no_answer_in_context`, and invalid service input was rejected with HTTP `422`.  
  Evidence: `reports/observed_ner_qa.json` and `BENCHMARKS.md`

- **Saved fallback from the same submission, if available:**  
  Saved notebook outputs and JSON evidence are stored under `reports/`.

## 4. Measured evidence | الدليل المقاس

- **Quality metric, data split and report:**  
  Classification test Macro-F1 = **0.8667**  
  Transformer test accuracy = **0.875**  
  NER F1 = **0.5714**  
  Semantic Search Recall@3 = **1.0000**  
  Re-ranked MRR@3 = **0.7222**  
  Evidence: `EVALUATION_REPORT.md`, `PROJECT_SUMMARY.json`

- **Performance metric, environment and report:**  
  ONNX FP32 p95 latency = **9.541 ms**  
  Dynamic INT8 p95 latency = **7.922 ms**  
  INT8 prediction agreement = **1.0000**  
  Environment: CPU  
  Evidence: `BENCHMARKS.md`

- **Measurement label and limits:**  
  `MEASURED_SMOKE` / course-fixture results.  
  These results come from small educational datasets and should not be interpreted as production-quality benchmarks.

## 5. Decision and ownership | القرار والمساهمة

- **My change / measured extension and file:**  
  Measured cross-encoder re-ranking extension for bilingual semantic search.  
  Evidence: `reports/observed_reranking_display.json` and `DECISIONS.md`

- **Baseline, benefit/cost and limitation:**  
  Baseline MRR@3 = **0.6667**  
  Re-ranked MRR@3 = **0.7222**  
  Improvement = **+0.0556**  
  Decision = `ADOPT_FOR_EXPERIMENT`  
  Cost: additional re-ranking latency on CPU  
  Limitation: only 6 answerable test queries and a small course dataset

- **One code decision I can explain:**  
  I used L2-normalised multilingual sentence embeddings with FAISS `IndexFlatIP`, and selected the no-answer threshold using validation data only to reduce leakage.

The talk is five minutes plus two minutes of individual verification; up to five slides or equivalent. Presentation credit is 10 within the total of 100. Optional slides may be linked here; no paid tool is required.

العرض خمس دقائق ودقيقتان للتحقق الفردي، بخمس شرائح كحد أقصى أو ما يعادلها. درجة العرض 10 ضمن المجموع 100. يمكن ربط شرائح اختيارية هنا؛ لا تحتاج أداة مدفوعة.
