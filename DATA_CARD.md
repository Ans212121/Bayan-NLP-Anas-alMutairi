# DATA CARD — Bayan

**Student:** Anas Ibrahim Al-Mutairi  
**Program:** Applied Natural Language Processing  
**Program Code:** SDA-AIE-211  
**Project:** Bayan  
**Trainer:** Meaad Al-Marri  
**GitHub:** Ans212121  

## Dataset identity

- Name/version: Bayan course sample dataset / project dataset
- Source/creator: Bayan Applied NLP course materials by Meaad Al-Marri
- License/permission: Course-provided dataset for educational use within the Bayan Applied NLP program
- Data hash or immutable revision: Dataset provenance and project evidence are recorded in the repository reports
- Intended educational task: Arabic and English NLP experiments including text classification, NER, QA, semantic search, evaluation, and optimisation

## Composition

| Split | Rows | Arabic | English | Groups | Notes |
|---|---:|---:|---:|---:|---|
| train | 24 | 12 | 12 | 12 | grouped training split |
| validation | 8 | 4 | 4 | 4 | used for model and threshold selection |
| frozen test | 8 | 4 | 4 | 4 | evaluated after validation decisions were fixed |

## Fields and labels

| Field/label | Meaning | Allowed values | Missing-value rule |
|---|---|---|---|
| text | Input sentence | Arabic or English text | Required |
| language | Language of the example | ar, en | Required |
| topic | Topic classification label | digital_service, health, permit, transport | Required for topic classification |
| sentiment | Sentiment classification label | Values supplied by the course dataset | Required for sentiment classification |
| group_id | Group identifier used to prevent leakage | Dataset group identifier | Required for grouped splitting |
| split | Dataset partition | train, validation, test | Required |

## Collection/generation

The examples used in this project come from the Bayan Applied NLP course datasets and course fixtures provided for training purposes.

The dataset contains small Arabic and English examples designed for controlled educational NLP experiments.

The examples are used to demonstrate preprocessing, model training, evaluation, semantic search, error analysis, and optimisation.

The project does not claim that these examples represent production-scale or real-world language distributions.

## Cleaning and preprocessing

- Display copy rule: The original raw text is preserved separately from the model-ready text.
- PII masking rule: Email addresses are replaced with `<EMAIL>` and Saudi mobile-number patterns with `<PHONE>`.
- Arabic profile/version: Arabic text processing uses NFC Unicode normalisation, Tatweel removal, optional diacritic removal, and optional Alef normalisation.
- Deduplication/grouping: Examples are grouped using `group_id`, with groups isolated across train, validation, and test partitions.
- Filtering/exclusions: Invalid or unsupported inputs are rejected while preserving the original display copy.

## Split and leakage controls

- Split method/seed: Grouped train/validation/test split using random seed **42**.
- Group isolation evidence: Group overlap across dataset splits = **0**.
- Near-duplicate audit: Group-based isolation is used to reduce leakage from related examples.
- Frozen-test access: Test evaluation is performed after validation and model-selection decisions are fixed.
- Final submission commit: To be recorded when the final `submission-v1.0` version is created.

## Known gaps and risks

- Dialects/Arabizi: The dataset has limited coverage of Arabic dialects and Arabizi.
- Class balance: The dataset is small, so class-specific measurements may have high uncertainty.
- Synthetic-to-real gap: Educational course examples may not accurately represent real production traffic.
- Annotation ambiguity: Some examples may reasonably support more than one interpretation or label.
- Small slices/uncertainty: Validation and test slices are small, so reported measurements should not be treated as production-quality estimates.
- Misuse/privacy risk: Real personal or sensitive information should not be entered into the system. PII masking is included as an additional safeguard.

## Permitted and prohibited use

- Permitted educational use: Learning, experimentation, training, testing, evaluation, and demonstration within the Bayan Applied NLP project.
- Prohibited/high-risk use: Production decision-making, profiling real individuals, or processing sensitive personal information without additional safeguards and approval.
- Human review: Human review is required before any real-world or high-impact use of model outputs.

## Maintenance

- Project owner: Anas Ibrahim Al-Mutairi
- GitHub account: Ans212121
- Repository: Bayan-NLP-anas-al-mutairi
- Change/version policy: Project changes are tracked through Git commits and final submission tags.
- Index/model rebuild triggers: Models or indexes should be rerun when the dataset, preprocessing rules, model version, embeddings, classifier, or retrieval configuration changes.
