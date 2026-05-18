import csv
import json
import math
import random
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ANALYSIS = ROOT / "analysis" / "outputs"
SRC = ROOT / "src"
SEED = 73019


def money(value):
    return round(value, 2)


def pct(value):
    return round(value, 4)


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def safe_div(numerator, denominator):
    return numerator / denominator if denominator else 0


def build():
    random.seed(SEED)
    DATA.mkdir(exist_ok=True)
    ANALYSIS.mkdir(parents=True, exist_ok=True)

    partners = [
        ("P001", "SaaS platform", "Core", 1.18),
        ("P002", "ISO portfolio", "Core", 1.06),
        ("P003", "PayFac program", "Strategic", 1.24),
        ("P004", "Bank referral", "Strategic", 0.92),
        ("P005", "Vertical software", "Growth", 1.34),
        ("P006", "Marketplace", "Growth", 0.86),
        ("P007", "Unattended operator", "Watch", 0.72),
        ("P008", "Healthcare billing", "Watch", 0.95),
    ]
    channels = {
        "online": {"weight": 1.36, "latency": 420, "ticket": 74, "share": 0.34},
        "in_app": {"weight": 1.08, "latency": 380, "ticket": 52, "share": 0.18},
        "in_store": {"weight": 1.28, "latency": 300, "ticket": 43, "share": 0.24},
        "mobile": {"weight": 0.84, "latency": 450, "ticket": 39, "share": 0.12},
        "unattended": {"weight": 0.52, "latency": 560, "ticket": 18, "share": 0.07},
        "recurring": {"weight": 0.68, "latency": 410, "ticket": 61, "share": 0.05},
    }
    methods = {
        "card": {"auth": 0.905, "decline": 0.071, "return": 0.003, "ticket": 1.0, "mix": 0.58},
        "ach": {"auth": 0.942, "decline": 0.027, "return": 0.018, "ticket": 2.15, "mix": 0.14},
        "p2p": {"auth": 0.921, "decline": 0.046, "return": 0.009, "ticket": 0.64, "mix": 0.08},
        "wallet": {"auth": 0.931, "decline": 0.041, "return": 0.004, "ticket": 0.86, "mix": 0.15},
        "tokenized_card": {"auth": 0.948, "decline": 0.033, "return": 0.002, "ticket": 1.08, "mix": 0.05},
    }
    processors = {
        "processor_a": {"lift": 0.006, "variance": 0.82},
        "processor_b": {"lift": -0.004, "variance": 1.18},
        "processor_c": {"lift": 0.001, "variance": 1.02},
        "processor_d": {"lift": -0.009, "variance": 1.32},
    }
    processor_list = list(processors)
    start = date(2026, 1, 1)
    days = 120

    transaction_rows = []
    incident_rows = []
    reconciliation_rows = []
    partner_rows = []

    for partner_id, partner_type, segment, scale in partners:
        partner_rows.append(
            {
                "partner_id": partner_id,
                "partner_type": partner_type,
                "segment": segment,
                "primary_product_motion": random.choice(["gateway reporting", "routing controls", "ACH expansion", "merchant portal"]),
                "monthly_business_review_owner": random.choice(["product analytics", "product manager", "data insights", "support operations"]),
                "portfolio_scale_index": round(scale, 2),
            }
        )

    for day_offset in range(days):
        current = start + timedelta(days=day_offset)
        weekday_factor = 1.12 if current.weekday() in [1, 2, 3] else 0.92
        month_factor = 1 + (day_offset / days) * 0.11
        seasonal = 1 + math.sin(day_offset / 11) * 0.04
        for partner_id, partner_type, segment, scale in partners:
            for channel, channel_meta in channels.items():
                for method, method_meta in methods.items():
                    if channel == "unattended" and method in ["ach", "p2p"]:
                        continue
                    if channel == "recurring" and method == "p2p":
                        continue
                    processor = random.choices(
                        processor_list,
                        weights=[0.34, 0.26, 0.27, 0.13],
                        k=1,
                    )[0]
                    base_count = 1100 * scale * channel_meta["share"] * method_meta["mix"]
                    noise = random.uniform(0.86, 1.17)
                    tx_count = max(18, int(base_count * weekday_factor * month_factor * seasonal * noise))
                    avg_ticket = channel_meta["ticket"] * method_meta["ticket"] * random.uniform(0.9, 1.13)
                    gross_volume = tx_count * avg_ticket
                    auth_rate = method_meta["auth"] + processors[processor]["lift"] + random.uniform(-0.015, 0.014)
                    if processor == "processor_d" and method == "ach" and day_offset in range(58, 70):
                        auth_rate -= 0.036
                    if partner_id == "P007" and channel == "unattended" and day_offset in range(74, 91):
                        auth_rate -= 0.029
                    auth_rate = max(0.82, min(0.982, auth_rate))
                    decline_rate = max(0.006, 1 - auth_rate - random.uniform(0.018, 0.041))
                    return_rate = max(0, method_meta["return"] + random.uniform(-0.002, 0.004))
                    capture_rate = max(0.88, min(0.996, auth_rate - random.uniform(0.004, 0.018)))
                    chargeback_rate = max(0.0002, random.uniform(0.0006, 0.006) * (1.5 if channel == "online" else 1))
                    latency = channel_meta["latency"] * processors[processor]["variance"] * random.uniform(0.84, 1.22)
                    settlement_delay = random.uniform(14, 38)
                    if method == "ach":
                        settlement_delay += random.uniform(16, 42)
                    if processor == "processor_d":
                        settlement_delay += random.uniform(6, 19)
                    recon_variance = gross_volume * random.uniform(-0.0009, 0.0014)
                    if method == "ach" and processor == "processor_d" and day_offset in range(58, 70):
                        recon_variance += gross_volume * random.uniform(0.004, 0.008)
                    data_quality_score = 98 - abs(recon_variance / max(gross_volume, 1)) * 2100 - random.uniform(0, 4.6)
                    if channel == "recurring" and day_offset in range(34, 42):
                        data_quality_score -= random.uniform(7, 13)
                    data_quality_score = max(62, min(99.6, data_quality_score))
                    revenue_take_rate = 0.0062 if method == "card" else 0.0047 if method == "ach" else 0.0056
                    net_revenue = gross_volume * revenue_take_rate
                    transaction_rows.append(
                        {
                            "date": current.isoformat(),
                            "partner_id": partner_id,
                            "partner_segment": segment,
                            "channel": channel,
                            "payment_method": method,
                            "processor": processor,
                            "transaction_count": tx_count,
                            "gross_volume": money(gross_volume),
                            "net_revenue": money(net_revenue),
                            "authorization_rate": pct(auth_rate),
                            "capture_rate": pct(capture_rate),
                            "decline_rate": pct(decline_rate),
                            "return_rate": pct(return_rate),
                            "chargeback_rate": pct(chargeback_rate),
                            "gateway_latency_ms": int(latency),
                            "settlement_delay_hours": round(settlement_delay, 1),
                            "reconciliation_variance": money(recon_variance),
                            "data_quality_score": round(data_quality_score, 1),
                        }
                    )

                    if random.random() < 0.018 or data_quality_score < 78 or abs(recon_variance) > gross_volume * 0.004:
                        issue_type = random.choice(
                            [
                                "missing webhook",
                                "ACH return spike",
                                "ledger variance",
                                "processor latency",
                                "duplicate transaction event",
                                "batch settlement delay",
                            ]
                        )
                        severity = "high" if data_quality_score < 78 or abs(recon_variance) > gross_volume * 0.004 else random.choice(["medium", "low"])
                        incident_rows.append(
                            {
                                "incident_id": f"INC{len(incident_rows)+1:04d}",
                                "opened_date": current.isoformat(),
                                "partner_id": partner_id,
                                "channel": channel,
                                "payment_method": method,
                                "processor": processor,
                                "issue_type": issue_type,
                                "severity": severity,
                                "estimated_transactions_at_risk": int(tx_count * random.uniform(0.08, 0.36)),
                                "estimated_volume_at_risk": money(gross_volume * random.uniform(0.04, 0.22)),
                                "owner": random.choice(["data insights", "product engineering", "support operations", "finance operations"]),
                                "status": random.choice(["triage", "root cause found", "fix queued", "monitoring"]),
                            }
                        )

                    if day_offset % 7 == 0 and method in ["ach", "card"]:
                        reconciliation_rows.append(
                            {
                                "week_start": current.isoformat(),
                                "partner_id": partner_id,
                                "payment_method": method,
                                "processor": processor,
                                "gateway_settled_volume": money(gross_volume * 7 * random.uniform(0.96, 1.04)),
                                "ledger_booked_volume": money(gross_volume * 7 * random.uniform(0.958, 1.043)),
                                "unmatched_batches": random.randint(0, 5 if method == "ach" else 3),
                                "oldest_unmatched_hours": round(random.uniform(4, 92 if method == "ach" else 44), 1),
                                "finance_confidence": random.choice(["certified", "watch", "needs research"]),
                            }
                        )

    experiments = [
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
        },
    ]

    aggregates = defaultdict(lambda: defaultdict(float))
    daily_totals = defaultdict(lambda: {"gross_volume": 0, "transaction_count": 0, "net_revenue": 0})
    for row in transaction_rows:
        key = (row["channel"], row["payment_method"])
        aggregates[key]["gross_volume"] += float(row["gross_volume"])
        aggregates[key]["transaction_count"] += int(row["transaction_count"])
        aggregates[key]["net_revenue"] += float(row["net_revenue"])
        aggregates[key]["auth_weighted"] += float(row["authorization_rate"]) * int(row["transaction_count"])
        aggregates[key]["quality_weighted"] += float(row["data_quality_score"]) * int(row["transaction_count"])
        aggregates[key]["recon_abs"] += abs(float(row["reconciliation_variance"]))
        aggregates[key]["settlement_weighted"] += float(row["settlement_delay_hours"]) * int(row["transaction_count"])
        daily_totals[row["date"]]["gross_volume"] += float(row["gross_volume"])
        daily_totals[row["date"]]["transaction_count"] += int(row["transaction_count"])
        daily_totals[row["date"]]["net_revenue"] += float(row["net_revenue"])

    opportunity_rows = []
    for (channel, method), values in aggregates.items():
        tx = values["transaction_count"]
        auth_rate = safe_div(values["auth_weighted"], tx)
        quality = safe_div(values["quality_weighted"], tx)
        settlement = safe_div(values["settlement_weighted"], tx)
        target_auth = 0.935 if method != "ach" else 0.955
        auth_gap_bps = max(0, (target_auth - auth_rate) * 10000)
        revenue_upside = values["gross_volume"] * min(auth_gap_bps / 10000, 0.018) * 0.006
        quality_penalty = max(0, 95 - quality) * 2.2
        recon_penalty = safe_div(values["recon_abs"], values["gross_volume"]) * 12000
        priority_score = auth_gap_bps * 0.42 + quality_penalty + recon_penalty + max(0, settlement - 34) * 0.8 + revenue_upside / 1200
        opportunity_rows.append(
            {
                "channel": channel,
                "payment_method": method,
                "transaction_count": int(tx),
                "gross_volume": money(values["gross_volume"]),
                "authorization_rate": pct(auth_rate),
                "data_quality_score": round(quality, 1),
                "reconciliation_variance_abs": money(values["recon_abs"]),
                "settlement_delay_hours": round(settlement, 1),
                "auth_gap_bps": round(auth_gap_bps, 1),
                "estimated_revenue_upside": money(revenue_upside),
                "priority_score": round(priority_score, 1),
            }
        )
    opportunity_rows.sort(key=lambda item: item["priority_score"], reverse=True)

    incident_summary = defaultdict(lambda: {"count": 0, "volume": 0, "high": 0})
    for incident in incident_rows:
        key = (incident["issue_type"], incident["owner"])
        incident_summary[key]["count"] += 1
        incident_summary[key]["volume"] += float(incident["estimated_volume_at_risk"])
        incident_summary[key]["high"] += 1 if incident["severity"] == "high" else 0
    integrity_rows = []
    for (issue_type, owner), values in incident_summary.items():
        integrity_rows.append(
            {
                "issue_type": issue_type,
                "owner": owner,
                "incident_count": values["count"],
                "high_severity_count": values["high"],
                "estimated_volume_at_risk": money(values["volume"]),
                "risk_score": round(values["high"] * 18 + values["count"] * 4 + values["volume"] / 180000, 1),
            }
        )
    integrity_rows.sort(key=lambda item: item["risk_score"], reverse=True)

    forecast_rows = []
    sorted_days = sorted(daily_totals)
    last_28 = sorted_days[-28:]
    first_28 = sorted_days[:28]
    baseline_daily_volume = safe_div(sum(daily_totals[d]["gross_volume"] for d in last_28), len(last_28))
    early_daily_volume = safe_div(sum(daily_totals[d]["gross_volume"] for d in first_28), len(first_28))
    growth_rate = max(0.005, min(0.14, (baseline_daily_volume / early_daily_volume - 1) / 4))
    for month in range(1, 7):
        projected_volume = baseline_daily_volume * 30 * ((1 + growth_rate) ** month)
        projected_revenue = projected_volume * 0.0058
        forecast_rows.append(
            {
                "forecast_month": f"month_{month}",
                "projected_volume": money(projected_volume),
                "projected_net_revenue": money(projected_revenue),
                "assumed_monthly_growth_rate": pct(growth_rate),
            }
        )

    experiment_rows = []
    for experiment in experiments:
        annualized_revenue_upside = experiment["eligible_volume"] * (experiment["expected_lift_bps"] / 10000) * 0.006 * 12
        readiness_modifier = 1 if experiment["readiness"] == "ready" else 0.72 if "QA" in experiment["readiness"] else 0.54
        experiment_rows.append(
            {
                **experiment,
                "eligible_volume": money(experiment["eligible_volume"]),
                "annualized_revenue_upside": money(annualized_revenue_upside),
                "priority_score": round(annualized_revenue_upside / 1000 * experiment["confidence"] * readiness_modifier, 1),
            }
        )
    experiment_rows.sort(key=lambda item: item["priority_score"], reverse=True)

    total_volume = sum(float(row["gross_volume"]) for row in transaction_rows)
    total_tx = sum(int(row["transaction_count"]) for row in transaction_rows)
    total_revenue = sum(float(row["net_revenue"]) for row in transaction_rows)
    weighted_auth = safe_div(sum(float(row["authorization_rate"]) * int(row["transaction_count"]) for row in transaction_rows), total_tx)
    weighted_quality = safe_div(sum(float(row["data_quality_score"]) * int(row["transaction_count"]) for row in transaction_rows), total_tx)
    ach_rows = [row for row in transaction_rows if row["payment_method"] == "ach"]
    ach_return_rate = safe_div(sum(float(row["return_rate"]) * int(row["transaction_count"]) for row in ach_rows), sum(int(row["transaction_count"]) for row in ach_rows))
    summary = {
        "total_volume": money(total_volume),
        "total_transactions": int(total_tx),
        "net_revenue": money(total_revenue),
        "authorization_rate": pct(weighted_auth),
        "data_quality_score": round(weighted_quality, 1),
        "ach_return_rate": pct(ach_return_rate),
        "open_incidents": len(incident_rows),
        "high_severity_incidents": sum(1 for row in incident_rows if row["severity"] == "high"),
        "forecast_growth_rate": pct(growth_rate),
        "top_opportunity": opportunity_rows[0],
        "top_integrity_risk": integrity_rows[0],
        "top_experiment": experiment_rows[0],
    }

    write_csv(DATA / "partners.csv", partner_rows, list(partner_rows[0].keys()))
    write_csv(DATA / "transaction_daily.csv", transaction_rows, list(transaction_rows[0].keys()))
    write_csv(DATA / "data_quality_incidents.csv", incident_rows, list(incident_rows[0].keys()))
    write_csv(DATA / "reconciliation_checks.csv", reconciliation_rows, list(reconciliation_rows[0].keys()))
    write_csv(DATA / "experiments.csv", experiment_rows, list(experiment_rows[0].keys()))
    write_csv(ANALYSIS / "opportunity_queue.csv", opportunity_rows, list(opportunity_rows[0].keys()))
    write_csv(ANALYSIS / "integrity_queue.csv", integrity_rows, list(integrity_rows[0].keys()))
    write_csv(ANALYSIS / "experiment_readiness.csv", experiment_rows, list(experiment_rows[0].keys()))
    write_csv(ANALYSIS / "forecast_summary.csv", forecast_rows, list(forecast_rows[0].keys()))

    with (ANALYSIS / "kpi_summary.json").open("w") as handle:
        json.dump(summary, handle, indent=2)

    app_data = {
        "summary": summary,
        "opportunityQueue": opportunity_rows[:8],
        "integrityQueue": integrity_rows[:8],
        "experiments": experiment_rows,
        "forecast": forecast_rows,
        "paymentMix": sorted(
            [
                {
                    "payment_method": method,
                    "gross_volume": money(sum(float(row["gross_volume"]) for row in transaction_rows if row["payment_method"] == method)),
                    "transactions": sum(int(row["transaction_count"]) for row in transaction_rows if row["payment_method"] == method),
                }
                for method in methods
            ],
            key=lambda row: row["gross_volume"],
            reverse=True,
        ),
        "channelMix": sorted(
            [
                {
                    "channel": channel,
                    "gross_volume": money(sum(float(row["gross_volume"]) for row in transaction_rows if row["channel"] == channel)),
                    "authorization_rate": pct(
                        safe_div(
                            sum(float(row["authorization_rate"]) * int(row["transaction_count"]) for row in transaction_rows if row["channel"] == channel),
                            sum(int(row["transaction_count"]) for row in transaction_rows if row["channel"] == channel),
                        )
                    ),
                }
                for channel in channels
            ],
            key=lambda row: row["gross_volume"],
            reverse=True,
        ),
    }
    with (SRC / "data.js").open("w") as handle:
        handle.write("window.GATEWAY_DATA = ")
        json.dump(app_data, handle, indent=2)
        handle.write(";\n")


if __name__ == "__main__":
    build()
