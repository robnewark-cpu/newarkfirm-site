/**
 * Server-side HTML renderer for the cases dashboard.
 *
 * Phase 2 fixes applied in UI:
 *  - "New since" header label changed to "Last ingested" to avoid confusion
 *    with filing date (Aviation was showing "new since Nov 9, 2026" while
 *    newest filing was Oct 16, 2026).
 *  - State scope shown from desk.stateScope (truthful — Aviation now shows
 *    "All federal districts" not "TX/OK/AR/CO/NM").
 *  - Count displayed is the live D1 count, not the cached overview_count.
 */

import { DeskConfig } from "../desks/config";
import { QueueRow } from "../api/ingest";

const CSS = `
  :root {
    --bg: #f8f9fa; --surface: #fff; --border: #dee2e6;
    --primary: #1a3a5c; --accent: #c8913a; --text: #212529;
    --muted: #6c757d; --danger: #dc3545; --success: #198754;
    --warn: #ffc107;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); }
  a { color: var(--primary); text-decoration: none; }
  a:hover { text-decoration: underline; }
  header { background: var(--primary); color: #fff; padding: 1rem 2rem;
           display: flex; align-items: center; gap: 1rem; }
  header h1 { font-size: 1.25rem; font-weight: 700; }
  header span { font-size: .85rem; opacity: .75; }
  main { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }
  .desk-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px,1fr)); gap: 1rem; }
  .desk-card { background: var(--surface); border: 1px solid var(--border);
               border-radius: 8px; padding: 1.25rem; }
  .desk-card h2 { font-size: 1rem; font-weight: 700; margin-bottom: .5rem; }
  .desk-card .meta { font-size: .8rem; color: var(--muted); margin-bottom: .75rem; }
  .desk-card .count { font-size: 1.5rem; font-weight: 700; color: var(--primary); }
  .desk-card .stalled { color: var(--danger); font-size: .75rem; font-weight: 600;
                        margin-top: .25rem; }
  .desk-card .fixed { color: var(--success); font-size: .75rem; font-weight: 600;
                      margin-top: .25rem; }
  .btn { display: inline-block; padding: .5rem 1rem; border-radius: 4px; font-size: .875rem;
         font-weight: 600; cursor: pointer; border: none; }
  .btn-primary { background: var(--primary); color: #fff; }
  .btn-primary:hover { background: #122b47; }
  .btn-refresh { background: var(--accent); color: #fff; margin-top: .75rem; }
  .desk-header { display: flex; align-items: flex-start; justify-content: space-between;
                 margin-bottom: 1.5rem; gap: 1rem; flex-wrap: wrap; }
  .desk-header h1 { font-size: 1.5rem; }
  .desk-header .info { font-size: .85rem; color: var(--muted); margin-top: .25rem; }
  table { width: 100%; border-collapse: collapse; background: var(--surface);
          border-radius: 8px; overflow: hidden; }
  th { background: var(--primary); color: #fff; text-align: left;
       padding: .625rem .75rem; font-size: .8rem; font-weight: 600; }
  td { padding: .625rem .75rem; font-size: .8rem; border-bottom: 1px solid var(--border); }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: #f1f3f5; }
  .badge { display: inline-block; padding: .2em .5em; border-radius: 4px;
           font-size: .7rem; font-weight: 600; }
  .badge-new { background: #cfe2ff; color: #084298; }
  .badge-open { background: #d1e7dd; color: #0f5132; }
  .badge-warn { background: #fff3cd; color: #664d03; }
  .pagination { display: flex; gap: .5rem; margin-top: 1rem; align-items: center; }
  .nos-warn { background: #fff3cd; border: 1px solid #ffc107; border-radius: 4px;
              padding: .75rem 1rem; font-size: .85rem; margin-bottom: 1rem; }
`;

export function renderDashboard(
  desks: DeskConfig[],
  metaMap: Record<string, {
    last_ingest_at: string | null;
    overview_count: number;
    alert_status: string;
  } | undefined>
): string {
  const cards = desks
    .map((d) => {
      const meta = metaMap[d.id];
      const count = meta?.overview_count ?? 0;
      const lastIngest = meta?.last_ingest_at
        ? new Date(meta.last_ingest_at).toLocaleDateString()
        : "Never";
      const alertOk = meta?.alert_status === "live";

      return `
      <div class="desk-card">
        <h2><a href="/desk/${d.id}">${d.label}</a></h2>
        <div class="meta">
          NOS: ${d.nosFilter.join(", ")} · ${d.stateScope}
        </div>
        <div class="count">${count}</div>
        <div style="font-size:.75rem;color:var(--muted)">matters</div>
        ${
          d.wasStalled && alertOk
            ? `<div class="fixed">✓ Feed restored</div>`
            : d.wasStalled
            ? `<div class="stalled">⚠ Feed stalled — check alert</div>`
            : `<div style="font-size:.75rem;color:var(--success)">● Live</div>`
        }
        <div class="meta" style="margin-top:.5rem">Last ingested: ${lastIngest}</div>
        <a href="/desk/${d.id}" class="btn btn-primary" style="margin-top:.75rem;display:block;text-align:center">
          View queue
        </a>
      </div>`;
    })
    .join("");

  return `<!doctype html><html lang="en"><head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Case Desks — Newark Firm</title>
    <style>${CSS}</style>
  </head><body>
    <header>
      <h1>Newark Firm — Case Desks</h1>
      <span>Docket alert monitor · ${new Date().toLocaleDateString()}</span>
    </header>
    <main>
      <h2 style="margin-bottom:1rem">All Desks</h2>
      <div class="desk-grid">${cards}</div>
    </main>
  </body></html>`;
}

export function renderDeskPage(
  desk: DeskConfig,
  rows: QueueRow[],
  total: number,
  liveCount: number,
  offset: number,
  meta: {
    last_ingest_at: string | null;
    alert_status: string;
    overview_count: number;
  } | null | undefined
): string {
  // Phase 2 count consistency: display liveCount (from D1 COUNT(*)) not cached value
  const displayCount = liveCount;

  // Phase 2: "Last ingested" label — not "new since" / not a filing date
  const lastIngestedLabel = meta?.last_ingest_at
    ? new Date(meta.last_ingest_at).toLocaleString()
    : "Never";

  const newestFiling = rows.length > 0
    ? rows.reduce((a, b) =>
        a.date_filed > b.date_filed ? a : b
      ).date_filed
    : null;

  const alertStatusBadge =
    meta?.alert_status === "live"
      ? `<span class="badge badge-new">Live</span>`
      : meta?.alert_status === "paused"
      ? `<span class="badge badge-warn">⚠ Paused</span>`
      : `<span class="badge" style="background:#f8d7da;color:#842029">Unknown</span>`;

  const tableRows = rows
    .map((r) => {
      const counsel = r.defendant_counsel
        ? escHtml(r.defendant_counsel)
        : "<em style='color:var(--muted)'>not listed</em>";

      return `<tr>
        <td><a href="https://www.courtlistener.com/docket/${r.docket_id}/" target="_blank" rel="noopener">
          ${escHtml(r.case_number)}
        </a></td>
        <td>${escHtml(r.case_name)}</td>
        <td>${escHtml(r.court)}</td>
        <td>${r.nos_code}</td>
        <td>${r.date_filed}</td>
        <td>${counsel}</td>
        <td><span class="badge badge-${r.status === 'new' ? 'new' : 'open'}">${escHtml(r.status)}</span></td>
      </tr>`;
    })
    .join("");

  const prevOffset = Math.max(0, offset - desk.queuePageSize);
  const nextOffset = offset + desk.queuePageSize;
  const hasPrev = offset > 0;
  const hasNext = nextOffset < total;

  const pagination =
    total > desk.queuePageSize
      ? `<div class="pagination">
          ${hasPrev ? `<a class="btn btn-primary" href="/desk/${desk.id}?offset=${prevOffset}">← Previous</a>` : ""}
          <span style="font-size:.85rem;color:var(--muted)">
            Showing ${offset + 1}–${Math.min(offset + rows.length, total)} of ${total}
          </span>
          ${hasNext ? `<a class="btn btn-primary" href="/desk/${desk.id}?offset=${nextOffset}">Next →</a>` : ""}
        </div>`
      : "";

  const nosWarning =
    desk.id === "maritime"
      ? `<div class="nos-warn">
          <strong>⚠ Non-matching NOS rows may exist</strong> — run
          <a href="/api/desk/maritime/nos-audit" target="_blank">NOS audit</a>
          to review rows ingested before filter enforcement.
        </div>`
      : "";

  return `<!doctype html><html lang="en"><head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>${escHtml(desk.label)} Desk — Newark Firm</title>
    <style>${CSS}</style>
  </head><body>
    <header>
      <h1><a href="/" style="color:#fff">← Newark Firm</a></h1>
      <span>${escHtml(desk.label)} Desk</span>
    </header>
    <main>
      <div class="desk-header">
        <div>
          <h1>${escHtml(desk.label)} Desk</h1>
          <div class="info">
            NOS: ${desk.nosFilter.join(", ")} ·
            ${escHtml(desk.stateScope)} ·
            ${displayCount} matter${displayCount !== 1 ? "s" : ""} ·
            Alert: ${alertStatusBadge}
          </div>
          <div class="info" style="margin-top:.25rem">
            Last ingested: ${escHtml(lastIngestedLabel)}
            ${newestFiling ? ` · Newest filing: ${escHtml(newestFiling)}` : ""}
          </div>
        </div>
        <button
          class="btn btn-refresh"
          onclick="refreshDesk('${desk.id}')"
          id="refresh-btn"
        >↻ Refresh this desk</button>
      </div>

      ${nosWarning}

      <table>
        <thead>
          <tr>
            <th>Case No.</th>
            <th>Case Name</th>
            <th>Court</th>
            <th>NOS</th>
            <th>Filed</th>
            <th>Counsel (Defendant)</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>${tableRows || '<tr><td colspan="7" style="text-align:center;padding:2rem;color:var(--muted)">No filings in queue yet. Try refreshing.</td></tr>'}</tbody>
      </table>

      ${pagination}
    </main>
    <script>
      async function refreshDesk(id) {
        const btn = document.getElementById('refresh-btn');
        btn.disabled = true;
        btn.textContent = '↻ Refreshing…';
        try {
          const r = await fetch('/api/desk/' + id + '/refresh', { method: 'POST' });
          const d = await r.json();
          if (d.inserted > 0) {
            btn.textContent = '✓ ' + d.inserted + ' new filing' + (d.inserted !== 1 ? 's' : '') + ' — reloading';
            setTimeout(() => location.reload(), 1200);
          } else {
            btn.textContent = '✓ No new filings';
            setTimeout(() => { btn.disabled = false; btn.textContent = '↻ Refresh this desk'; }, 2000);
          }
        } catch(e) {
          btn.textContent = '✗ Refresh failed';
          setTimeout(() => { btn.disabled = false; btn.textContent = '↻ Refresh this desk'; }, 2000);
        }
      }
    </script>
  </body></html>`;
}

function escHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}
