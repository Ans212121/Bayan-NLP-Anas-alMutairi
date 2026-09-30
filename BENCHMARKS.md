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

## Historical SYSTEMS_SMOKE values

| Candidate | Size | model-only p95 | Prediction agreement |
|---|---:|---:|---:|
| PyTorch parameters | 16.732 MiB | runtime-dependent | reference |
| ONNX FP32 | 16.788 MiB | 9.541 ms in preserved summary | 1.0000 |
| Dynamic INT8 | 4.287 MiB | 7.922 ms in preserved summary | 1.0000 |

ONNX FP32 max absolute logits difference: `1.639e-07`.

The old notebook decision `ADOPT_INT8` was scoped as:

`SYSTEMS_SMOKE_NOT_A_SHIP_DECISION`

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
