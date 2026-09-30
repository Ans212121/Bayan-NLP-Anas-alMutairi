# BENCHMARKS — Bayan

## Current evidence boundary

The previously saved Day 4 run is **SYSTEMS_SMOKE**, not a final project benchmark.

It used the course smoke model and successfully demonstrated:
- ONNX export/checker;
- ONNX numerical parity;
- dynamic INT8 quantisation attempt;
- FastAPI/TestClient contract;
- Arabic/English canaries;
- invalid-input rejection.

The notebook explicitly printed:

`NEXT_REQUIRED_FOR_GATE_D=RERUN_WITH_PROJECT_ARTIFACT_AND_FULL_WORKLOAD`

Therefore the values below are retained only as historical smoke evidence and are **not** used to declare Gate D complete.

## Historical SYSTEMS_SMOKE evidence

See original cells 114 and 119–128 in `reports/historical_evidence.txt` for the actual saved output. The automatic ADOPT_INT8 decision was explicitly `SYSTEMS_SMOKE_NOT_A_SHIP_DECISION`; it is not a project release decision.

## Gate D — corrected PROJECT_ARTIFACT run

Corrected Notebook 08 is prepared to load the student's saved Bayan topic checkpoint and the matching validation workload from Google Drive.

The clean run must record:
- exact model/checkpoint and preprocessing version;
- workload rows and hash;
- CPU/runtime/library versions;
- warm-up excluded;
- at least 30 measured repetitions;
- p50 / p95 / p99;
- throughput;
- observed process memory;
- task Macro-F1 for PyTorch / ONNX / INT8;
- quality tax relative to PyTorch;
- explicit ADOPT / REJECT / KEEP FP32 decision;
- FP32 rollback path.

Final project evidence will be written by the corrected notebook to:

- `reports/benchmark_results.json`
- `reports/service_smoke.json`

## Required measured extension — batch endpoint

The R7 extension is **batch endpoint**, not cross-encoder re-ranking.

Corrected Notebook 08 compares:
1. sequential single-item service calls;
2. a true batch model call on the same examples.

It performs warm-up, 30 measured repetitions, verifies prediction agreement, measures latency/throughput trade-off and records an evidence-based ADOPT/REJECT decision.

Final extension evidence path:

`reports/extension_batch_endpoint.json`

## Status

**PROJECT_ARTIFACT benchmark: PENDING_CLEAN_RUN**

No `MEASURED` PROJECT_ARTIFACT numbers are claimed until the corrected Notebook 08 is run successfully in Colab and its generated JSON reports are committed.


## Measurement boundaries

`reports/extension_batch_endpoint.json` currently contains an explicit UNMEASURED status, not benchmark evidence. Corrected 08 replaces it only after real calls. Memory is observed process RSS in one shared runtime, not isolated per-candidate peak allocations. Batch timing is in-process TestClient whole-workload latency, not external-network latency or the cohort's 16-concurrent-request criterion. Project checkpoint quality remains a tiny-sample MEASURED_SMOKE estimate.

The configurable budget is reviewed before measurement (`BUDGET_CONFIRMED=True`). Training and serving share `bayan-protected-nfc/1.0.0` and max length 64. The report includes runtime commit, training commit, checkpoint state hash and workload hash.
