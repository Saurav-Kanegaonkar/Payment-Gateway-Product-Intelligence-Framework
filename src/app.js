const data = window.GATEWAY_DATA;

const money = (value) =>
  new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: value >= 1000000 ? 1 : 0,
    notation: value >= 1000000 ? "compact" : "standard",
  }).format(value);

const number = (value) =>
  new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 }).format(value);

const percent = (value, digits = 1) => `${(value * 100).toFixed(digits)}%`;

const label = (value) => String(value).replaceAll("_", " ");

function renderBars(items, key, labelKey) {
  const max = Math.max(...items.map((item) => item[key]));
  return items
    .map(
      (item) => `
        <li>
          <span>${label(item[labelKey])}</span>
          <strong>${money(item[key])}</strong>
          <i style="width:${Math.max(8, (item[key] / max) * 100)}%"></i>
        </li>
      `,
    )
    .join("");
}

function renderRows(rows, columns) {
  return rows
    .map(
      (row) => `
        <tr>
          ${columns
            .map((column) => `<td>${column.render ? column.render(row[column.key], row) : row[column.key]}</td>`)
            .join("")}
        </tr>
      `,
    )
    .join("");
}

function renderExperimentCards(experiments) {
  return experiments
    .map(
      (experiment) => `
        <article class="experiment-card">
          <div>
            <span>${experiment.experiment_id}</span>
            <b>${label(experiment.product_area)}</b>
          </div>
          <h3>${experiment.hypothesis}</h3>
          <dl>
            <div><dt>Primary metric</dt><dd>${label(experiment.primary_metric)}</dd></div>
            <div><dt>Readiness</dt><dd>${experiment.readiness}</dd></div>
            <div><dt>Annual upside</dt><dd>${money(experiment.annualized_revenue_upside)}</dd></div>
            <div><dt>Priority</dt><dd>${experiment.priority_score}</dd></div>
          </dl>
        </article>
      `,
    )
    .join("");
}

function renderForecast(rows) {
  const max = Math.max(...rows.map((row) => row.projected_volume));
  return rows
    .map(
      (row) => `
        <li>
          <span>${label(row.forecast_month)}</span>
          <i style="height:${Math.max(16, (row.projected_volume / max) * 100)}%"></i>
          <strong>${money(row.projected_volume)}</strong>
        </li>
      `,
    )
    .join("");
}

function renderApp() {
  const { summary } = data;
  document.querySelector("#app").innerHTML = `
    <header class="hero">
      <nav class="topbar" aria-label="Artifact sections">
        <a href="#cockpit">Cockpit</a>
        <a href="#integrity">Integrity</a>
        <a href="#experiments">Experiments</a>
      </nav>
      <section class="hero-grid">
        <div>
          <p class="eyebrow">Payment gateway product analytics</p>
          <h1>Product Intelligence Framework</h1>
          <p class="hero-copy">A decision workbench for gateway product teams that need trusted KPIs, transaction integrity monitoring, opportunity sizing, and experiment-ready roadmap evidence.</p>
        </div>
        <aside class="operating-brief">
          <span>Monthly operating question</span>
          <strong>Where should product, engineering, data, and finance focus to grow approved volume without weakening reporting trust?</strong>
        </aside>
      </section>
    </header>

    <main>
      <section class="metric-strip" aria-label="Gateway KPI summary">
        <article><span>Total volume</span><strong>${money(summary.total_volume)}</strong><em>modeled 120 days</em></article>
        <article><span>Transactions</span><strong>${number(summary.total_transactions)}</strong><em>synthetic events</em></article>
        <article><span>Authorization</span><strong>${percent(summary.authorization_rate)}</strong><em>weighted rate</em></article>
        <article><span>Data quality</span><strong>${summary.data_quality_score}</strong><em>score out of 100</em></article>
      </section>

      <section class="surface cockpit" id="cockpit">
        <div class="section-heading">
          <p class="eyebrow">Surface 1</p>
          <h2>Executive Product Cockpit</h2>
          <p>Shows product managers which payment methods, channels, and gateway capabilities are creating or blocking approved volume.</p>
        </div>
        <div class="cockpit-grid">
          <article class="panel large-panel">
            <div class="panel-title">
              <span>Opportunity queue</span>
              <strong>${label(summary.top_opportunity.channel)} ${label(summary.top_opportunity.payment_method)}</strong>
            </div>
            <table>
              <thead>
                <tr><th>Channel</th><th>Method</th><th>Auth gap</th><th>Quality</th><th>Upside</th></tr>
              </thead>
              <tbody>
                ${renderRows(data.opportunityQueue.slice(0, 6), [
                  { key: "channel", render: label },
                  { key: "payment_method", render: label },
                  { key: "auth_gap_bps", render: (value) => `${value} bps` },
                  { key: "data_quality_score" },
                  { key: "estimated_revenue_upside", render: money },
                ])}
              </tbody>
            </table>
          </article>
          <article class="panel">
            <div class="panel-title">
              <span>Payment mix</span>
              <strong>Volume by method</strong>
            </div>
            <ul class="bar-list">${renderBars(data.paymentMix, "gross_volume", "payment_method")}</ul>
          </article>
          <article class="panel">
            <div class="panel-title">
              <span>Channel health</span>
              <strong>Auth and volume</strong>
            </div>
            <ul class="channel-list">
              ${data.channelMix
                .map(
                  (item) => `
                    <li>
                      <span>${label(item.channel)}</span>
                      <strong>${percent(item.authorization_rate)}</strong>
                      <em>${money(item.gross_volume)}</em>
                    </li>
                  `,
                )
                .join("")}
            </ul>
          </article>
        </div>
      </section>

      <section class="surface integrity" id="integrity">
        <div class="section-heading">
          <p class="eyebrow">Surface 2</p>
          <h2>Transaction Integrity Monitor</h2>
          <p>Connects product analytics to reconciliation, ACH return monitoring, source freshness, and incident handoffs.</p>
        </div>
        <div class="integrity-grid">
          <article class="risk-card">
            <span>Top integrity risk</span>
            <strong>${summary.top_integrity_risk.issue_type}</strong>
            <p>${summary.top_integrity_risk.incident_count} incidents owned by ${summary.top_integrity_risk.owner}, with ${money(summary.top_integrity_risk.estimated_volume_at_risk)} in modeled volume at risk.</p>
          </article>
          <article class="risk-card">
            <span>ACH return rate</span>
            <strong>${percent(summary.ach_return_rate, 2)}</strong>
            <p>Tracked separately because ACH failure modes affect settlement confidence, partner reporting, and finance reconciliation.</p>
          </article>
          <article class="risk-card">
            <span>High severity incidents</span>
            <strong>${summary.high_severity_incidents}</strong>
            <p>Incidents are routed to data insights, product engineering, support operations, or finance operations based on root cause.</p>
          </article>
          <article class="panel wide-panel">
            <div class="panel-title">
              <span>Investigation queue</span>
              <strong>Grouped by issue and owner</strong>
            </div>
            <table>
              <thead>
                <tr><th>Issue</th><th>Owner</th><th>Incidents</th><th>High</th><th>Volume at risk</th></tr>
              </thead>
              <tbody>
                ${renderRows(data.integrityQueue.slice(0, 7), [
                  { key: "issue_type" },
                  { key: "owner" },
                  { key: "incident_count" },
                  { key: "high_severity_count" },
                  { key: "estimated_volume_at_risk", render: money },
                ])}
              </tbody>
            </table>
          </article>
        </div>
      </section>

      <section class="surface experiments" id="experiments">
        <div class="section-heading">
          <p class="eyebrow">Surface 3</p>
          <h2>Experimentation And Forecasting Lab</h2>
          <p>Turns ad hoc product questions into testable hypotheses, expected lift, forecast impact, and quarterly OKR evidence.</p>
        </div>
        <div class="experiment-layout">
          <article class="panel forecast-panel">
            <div class="panel-title">
              <span>Six month forecast</span>
              <strong>${percent(summary.forecast_growth_rate)} monthly growth assumption</strong>
            </div>
            <ul class="forecast-bars">${renderForecast(data.forecast)}</ul>
          </article>
          <div class="experiment-stack">${renderExperimentCards(data.experiments)}</div>
        </div>
      </section>
    </main>
  `;
}

renderApp();
