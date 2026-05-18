window.GATEWAY_DATA = {
  "summary": {
    "total_volume": 75078912.87,
    "total_transactions": 1230143,
    "net_revenue": 424804.97,
    "authorization_rate": 0.9184,
    "data_quality_score": 94.4,
    "ach_return_rate": 0.019,
    "open_incidents": 569,
    "high_severity_incidents": 51,
    "forecast_growth_rate": 0.01,
    "top_opportunity": {
      "channel": "unattended",
      "payment_method": "card",
      "transaction_count": 47701,
      "gross_volume": 872744.63,
      "authorization_rate": 0.9033,
      "data_quality_score": 94.5,
      "reconciliation_variance_abs": 524.25,
      "settlement_delay_hours": 28.0,
      "auth_gap_bps": 316.9,
      "estimated_revenue_upside": 94.26,
      "priority_score": 141.5
    },
    "top_integrity_risk": {
      "issue_type": "processor latency",
      "owner": "support operations",
      "incident_count": 32,
      "high_severity_count": 5,
      "estimated_volume_at_risk": 9512.72,
      "risk_score": 218.1
    },
    "top_experiment": {
      "experiment_id": "EXP001",
      "product_area": "smart routing",
      "hypothesis": "Route selected card-not-present transactions away from high-latency processors to improve authorization rate.",
      "primary_metric": "authorization_rate",
      "eligible_volume": 18400000,
      "expected_lift_bps": 42,
      "confidence": 0.78,
      "readiness": "ready",
      "okr_link": "Increase approved gateway volume",
      "annualized_revenue_upside": 5564.16,
      "priority_score": 4.3
    }
  },
  "opportunityQueue": [
    {
      "channel": "unattended",
      "payment_method": "card",
      "transaction_count": 47701,
      "gross_volume": 872744.63,
      "authorization_rate": 0.9033,
      "data_quality_score": 94.5,
      "reconciliation_variance_abs": 524.25,
      "settlement_delay_hours": 28.0,
      "auth_gap_bps": 316.9,
      "estimated_revenue_upside": 94.26,
      "priority_score": 141.5
    },
    {
      "channel": "recurring",
      "payment_method": "card",
      "transaction_count": 33588,
      "gross_volume": 2083527.94,
      "authorization_rate": 0.9047,
      "data_quality_score": 93.8,
      "reconciliation_variance_abs": 1248.63,
      "settlement_delay_hours": 27.3,
      "auth_gap_bps": 303.1,
      "estimated_revenue_upside": 225.02,
      "priority_score": 137.3
    },
    {
      "channel": "in_app",
      "payment_method": "card",
      "transaction_count": 122397,
      "gross_volume": 6467621.41,
      "authorization_rate": 0.9046,
      "data_quality_score": 94.4,
      "reconciliation_variance_abs": 4009.96,
      "settlement_delay_hours": 27.5,
      "auth_gap_bps": 304.3,
      "estimated_revenue_upside": 698.5,
      "priority_score": 137.1
    },
    {
      "channel": "online",
      "payment_method": "card",
      "transaction_count": 233635,
      "gross_volume": 17560740.77,
      "authorization_rate": 0.9047,
      "data_quality_score": 94.5,
      "reconciliation_variance_abs": 10389.94,
      "settlement_delay_hours": 27.7,
      "auth_gap_bps": 302.7,
      "estimated_revenue_upside": 1896.56,
      "priority_score": 136.9
    },
    {
      "channel": "in_store",
      "payment_method": "card",
      "transaction_count": 163441,
      "gross_volume": 7120783.42,
      "authorization_rate": 0.9049,
      "data_quality_score": 94.4,
      "reconciliation_variance_abs": 4354.02,
      "settlement_delay_hours": 27.6,
      "auth_gap_bps": 301.0,
      "estimated_revenue_upside": 769.04,
      "priority_score": 135.7
    },
    {
      "channel": "mobile",
      "payment_method": "card",
      "transaction_count": 81484,
      "gross_volume": 3230057.71,
      "authorization_rate": 0.9054,
      "data_quality_score": 94.4,
      "reconciliation_variance_abs": 1951.45,
      "settlement_delay_hours": 27.7,
      "auth_gap_bps": 296.4,
      "estimated_revenue_upside": 348.85,
      "priority_score": 133.3
    },
    {
      "channel": "in_store",
      "payment_method": "ach",
      "transaction_count": 39112,
      "gross_volume": 3663478.15,
      "authorization_rate": 0.9411,
      "data_quality_score": 94.3,
      "reconciliation_variance_abs": 2432.78,
      "settlement_delay_hours": 56.3,
      "auth_gap_bps": 139.0,
      "estimated_revenue_upside": 305.45,
      "priority_score": 85.9
    },
    {
      "channel": "online",
      "payment_method": "ach",
      "transaction_count": 55736,
      "gross_volume": 9024078.24,
      "authorization_rate": 0.9413,
      "data_quality_score": 94.3,
      "reconciliation_variance_abs": 5871.33,
      "settlement_delay_hours": 56.5,
      "auth_gap_bps": 136.7,
      "estimated_revenue_upside": 740.18,
      "priority_score": 85.4
    }
  ],
  "integrityQueue": [
    {
      "issue_type": "processor latency",
      "owner": "support operations",
      "incident_count": 32,
      "high_severity_count": 5,
      "estimated_volume_at_risk": 9512.72,
      "risk_score": 218.1
    },
    {
      "issue_type": "duplicate transaction event",
      "owner": "data insights",
      "incident_count": 30,
      "high_severity_count": 5,
      "estimated_volume_at_risk": 20822.82,
      "risk_score": 210.1
    },
    {
      "issue_type": "ACH return spike",
      "owner": "support operations",
      "incident_count": 30,
      "high_severity_count": 4,
      "estimated_volume_at_risk": 7657.43,
      "risk_score": 192.0
    },
    {
      "issue_type": "missing webhook",
      "owner": "data insights",
      "incident_count": 23,
      "high_severity_count": 5,
      "estimated_volume_at_risk": 9926.17,
      "risk_score": 182.1
    },
    {
      "issue_type": "ACH return spike",
      "owner": "product engineering",
      "incident_count": 24,
      "high_severity_count": 4,
      "estimated_volume_at_risk": 10251.82,
      "risk_score": 168.1
    },
    {
      "issue_type": "batch settlement delay",
      "owner": "product engineering",
      "incident_count": 28,
      "high_severity_count": 3,
      "estimated_volume_at_risk": 16686.7,
      "risk_score": 166.1
    },
    {
      "issue_type": "processor latency",
      "owner": "product engineering",
      "incident_count": 31,
      "high_severity_count": 2,
      "estimated_volume_at_risk": 9694.07,
      "risk_score": 160.1
    },
    {
      "issue_type": "batch settlement delay",
      "owner": "support operations",
      "incident_count": 35,
      "high_severity_count": 1,
      "estimated_volume_at_risk": 18468.88,
      "risk_score": 158.1
    }
  ],
  "experiments": [
    {
      "experiment_id": "EXP001",
      "product_area": "smart routing",
      "hypothesis": "Route selected card-not-present transactions away from high-latency processors to improve authorization rate.",
      "primary_metric": "authorization_rate",
      "eligible_volume": 18400000,
      "expected_lift_bps": 42,
      "confidence": 0.78,
      "readiness": "ready",
      "okr_link": "Increase approved gateway volume",
      "annualized_revenue_upside": 5564.16,
      "priority_score": 4.3
    },
    {
      "experiment_id": "EXP005",
      "product_area": "webhook resiliency",
      "hypothesis": "Retry backoff and payload validation reduce missing webhook incidents for transaction lifecycle events.",
      "primary_metric": "data_quality_score",
      "eligible_volume": 12400000,
      "expected_lift_bps": 37,
      "confidence": 0.74,
      "readiness": "ready",
      "okr_link": "Raise trusted reporting coverage",
      "annualized_revenue_upside": 3303.36,
      "priority_score": 2.4
    },
    {
      "experiment_id": "EXP003",
      "product_area": "recurring billing",
      "hypothesis": "Token refresh prompts recover failed recurring card payments before merchant support tickets open.",
      "primary_metric": "capture_rate",
      "eligible_volume": 7600000,
      "expected_lift_bps": 55,
      "confidence": 0.66,
      "readiness": "ready",
      "okr_link": "Grow retained processing volume",
      "annualized_revenue_upside": 3009.6,
      "priority_score": 2.0
    },
    {
      "experiment_id": "EXP002",
      "product_area": "ACH reliability",
      "hypothesis": "Pre-settlement return risk checks reduce ACH returns without lowering successful debit volume.",
      "primary_metric": "return_rate",
      "eligible_volume": 9200000,
      "expected_lift_bps": 31,
      "confidence": 0.71,
      "readiness": "needs event QA",
      "okr_link": "Improve settlement trust",
      "annualized_revenue_upside": 2053.44,
      "priority_score": 1.0
    },
    {
      "experiment_id": "EXP004",
      "product_area": "reporting self service",
      "hypothesis": "Partner-facing KPI definitions reduce ad hoc performance inquiries and repeated manual pulls.",
      "primary_metric": "support_inquiry_rate",
      "eligible_volume": 5100000,
      "expected_lift_bps": 24,
      "confidence": 0.62,
      "readiness": "instrumentation gap",
      "okr_link": "Scale product stakeholder transparency",
      "annualized_revenue_upside": 881.28,
      "priority_score": 0.3
    }
  ],
  "forecast": [
    {
      "forecast_month": "month_1",
      "projected_volume": 19436594.52,
      "projected_net_revenue": 112732.25,
      "assumed_monthly_growth_rate": 0.01
    },
    {
      "forecast_month": "month_2",
      "projected_volume": 19631815.33,
      "projected_net_revenue": 113864.53,
      "assumed_monthly_growth_rate": 0.01
    },
    {
      "forecast_month": "month_3",
      "projected_volume": 19828996.92,
      "projected_net_revenue": 115008.18,
      "assumed_monthly_growth_rate": 0.01
    },
    {
      "forecast_month": "month_4",
      "projected_volume": 20028159.01,
      "projected_net_revenue": 116163.32,
      "assumed_monthly_growth_rate": 0.01
    },
    {
      "forecast_month": "month_5",
      "projected_volume": 20229321.47,
      "projected_net_revenue": 117330.06,
      "assumed_monthly_growth_rate": 0.01
    },
    {
      "forecast_month": "month_6",
      "projected_volume": 20432504.41,
      "projected_net_revenue": 118508.53,
      "assumed_monthly_growth_rate": 0.01
    }
  ],
  "paymentMix": [
    {
      "payment_method": "card",
      "gross_volume": 37335475.88,
      "transactions": 682246
    },
    {
      "payment_method": "ach",
      "gross_volume": 20042983.45,
      "transactions": 161713
    },
    {
      "payment_method": "wallet",
      "gross_volume": 8772241.44,
      "transactions": 188955
    },
    {
      "payment_method": "tokenized_card",
      "gross_volume": 5710291.03,
      "transactions": 107187
    },
    {
      "payment_method": "p2p",
      "gross_volume": 3217921.07,
      "transactions": 90042
    }
  ],
  "channelMix": [
    {
      "channel": "online",
      "gross_volume": 33608534.75,
      "authorization_rate": 0.917
    },
    {
      "channel": "in_store",
      "gross_volume": 13817543.63,
      "authorization_rate": 0.9175
    },
    {
      "channel": "in_app",
      "gross_volume": 12832558.62,
      "authorization_rate": 0.918
    },
    {
      "channel": "mobile",
      "gross_volume": 6862249.44,
      "authorization_rate": 0.9198
    },
    {
      "channel": "recurring",
      "gross_volume": 6471602.6,
      "authorization_rate": 0.9261
    },
    {
      "channel": "unattended",
      "gross_volume": 1486423.83,
      "authorization_rate": 0.9182
    }
  ]
};
