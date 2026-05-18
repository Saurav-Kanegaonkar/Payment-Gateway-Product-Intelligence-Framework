# Data Dictionary

| Table | Grain | Purpose |
|---|---|---|
| `partners.csv` | Partner portfolio | Segment, product motion, monthly review owner, and scale index. |
| `transaction_daily.csv` | Partner x day x channel x payment method x processor | Product KPI analysis for volume, net revenue, authorization, capture, decline, returns, chargebacks, latency, settlement delay, reconciliation variance, and data quality. |
| `data_quality_incidents.csv` | Incident | Operational investigation queue for missing webhooks, duplicate events, ACH return spikes, ledger variance, processor latency, and batch settlement delays. |
| `reconciliation_checks.csv` | Partner x week x payment method x processor | Settlement and ledger confidence checks for finance and product operations review. |
| `experiments.csv` | Product experiment | Hypothesis backlog with primary metric, eligible volume, expected lift, confidence, readiness, OKR linkage, and estimated upside. |
| `analysis/outputs/opportunity_queue.csv` | Channel x payment method | Ranked product opportunity queue based on authorization gap, quality, reconciliation, settlement, and revenue upside. |
| `analysis/outputs/integrity_queue.csv` | Issue type x owner | Ranked investigation queue based on incident frequency, severity, and volume at risk. |
| `analysis/outputs/forecast_summary.csv` | Forecast month | Six month volume and revenue projection from modeled recent run rate. |
