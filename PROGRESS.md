# PROGRESS — Bayan Gates A–E

**Student GitHub:** Ans212121  
**Repository:** https://github.com/Ans212121/Bayan-NLP-Anas-alMutairi  
**Correction cycle started:** 2026-09-30

The preserved monolithic student run is retained as evidence, but the nine trainer-starter notebook copies are being replaced with notebooks derived from the student's own work. A gate is not marked complete here until the corrected notebooks have a clean saved run and traceable evidence.

| Gate | Status | Required evidence | Current evidence / next action |
|---|---|---|---|
| A — ingest | 🟨 IN_PROGRESS | preprocessing tests + tokenizer decision | tokenizer decision now documented in `DECISIONS.md`; clean-run corrected 00–02 notebooks |
| B — tasks | 🟨 IN_PROGRESS | topic + sentiment + NER + QA evidence | topic/NER/QA preserved; separate sentiment head added to corrected Notebook 03 and must be run |
| C — search & truth | 🟨 IN_PROGRESS | search metrics + slices + taxonomy | exact slice/CI/taxonomy files now committed under `reports/`; clean-run corrected 05–07 notebooks |
| D — ship | 🟨 IN_PROGRESS | PROJECT_ARTIFACT benchmark + API tests + canaries | corrected Notebook 08 prepared for real project model; run required |
| E — submit | 🟨 IN_PROGRESS | validator + demo + final tag | run validators/preflight after all notebook runs; do not treat old assessed tag as corrected release |

## Preserved evidence from the student's actual run

- Topic: `reports/observed_classification.json`
- NER/QA: `reports/observed_ner_qa.json`
- Arabic profile: `reports/observed_arabic_profile.json`
- Search manifest: `reports/observed_search_manifest.json`
- Core re-ranking comparison: `reports/observed_reranking_display.json`
- Evaluation fixture: `reports/day3_evaluation_fixture.json`
- Slice table: `reports/day3_slice_report.csv`
- Error taxonomy: `reports/day3_error_taxonomy.csv`

## Runtime / run-all evidence to be refreshed

| Notebook | Expected marker after clean run | GitHub path |
|---|---|---|
| 00 | `BAYAN_ENV_READY = True` | `notebooks/00_runtime_doctor.ipynb` |
| 01 | `DAY1_NOTEBOOK1_CORE=PASS` | `notebooks/01_text_processing_tokenization.ipynb` |
| 02 | `DAY1_NOTEBOOK2_CORE=PASS` | `notebooks/02_attention_transformers.ipynb` |
| 03 | `DAY2_NOTEBOOK3_CORE=PASS` + separate sentiment evidence | `notebooks/03_text_classification.ipynb` |
| 04 | `DAY2_NOTEBOOK4_CORE=PASS` | `notebooks/04_ner_and_qa.ipynb` |
| 05 | `DAY3_NOTEBOOK5_CORE=PASS` | `notebooks/05_arabic_nlp.ipynb` |
| 06 | `DAY3_NOTEBOOK6_CORE=PASS` | `notebooks/06_semantic_search.ipynb` |
| 07 | `DAY3_NOTEBOOK7_CORE=PASS` | `notebooks/07_evaluation_error_analysis.ipynb` |
| 08 | `DAY4_NOTEBOOK8_CORE=PASS` with `PROJECT_ARTIFACT` | `notebooks/08_optimization_serving.ipynb` |

## Final release state

- Old assessed commit: `e6a4f3e0ba8478464ae8c24bd29f09df1d6c0026`
- Backup of the pre-correction main branch: `backup-before-2026-09-30-evaluation-fixes`
- Corrected final commit: **PENDING_AFTER_CLEAN_RUN**
- Corrected validator report: **PENDING_AFTER_CLEAN_RUN**
- Corrected preflight report: **PENDING_AFTER_CLEAN_RUN**
- Final-tag action: perform only after the corrected clean run and according to the trainer's resubmission instructions.
