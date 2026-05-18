-- Example warehouse checks for a payment gateway product analytics framework.

-- 1. Daily authorization health by channel and payment method.
select
  date,
  channel,
  payment_method,
  sum(transaction_count) as transactions,
  sum(gross_volume) as gross_volume,
  sum(authorization_rate * transaction_count) / nullif(sum(transaction_count), 0) as weighted_authorization_rate
from transaction_daily
group by 1, 2, 3;

-- 2. Reconciliation exceptions that should enter the product integrity review.
select
  week_start,
  partner_id,
  payment_method,
  processor,
  gateway_settled_volume,
  ledger_booked_volume,
  abs(gateway_settled_volume - ledger_booked_volume) as settlement_variance,
  unmatched_batches,
  oldest_unmatched_hours,
  finance_confidence
from reconciliation_checks
where finance_confidence <> 'certified'
   or unmatched_batches > 2
   or oldest_unmatched_hours > 48;

-- 3. Incident owner queue for proactive investigation.
select
  issue_type,
  owner,
  count(*) as incident_count,
  sum(case when severity = 'high' then 1 else 0 end) as high_severity_count,
  sum(estimated_volume_at_risk) as estimated_volume_at_risk
from data_quality_incidents
group by 1, 2
order by high_severity_count desc, estimated_volume_at_risk desc;

-- 4. Experiment backlog ready for quarterly product OKR review.
select
  experiment_id,
  product_area,
  primary_metric,
  eligible_volume,
  expected_lift_bps,
  confidence,
  readiness,
  annualized_revenue_upside
from experiments
order by priority_score desc;
