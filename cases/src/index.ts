/**
 * cases.newarkfirm.com — Cloudflare Worker
 *
 * Routes:
 *   GET  /                         → dashboard (all 8 desks overview)
 *   GET  /desk/:id                 → desk queue page
 *   GET  /api/desks                → JSON: all desk configs + meta
 *   GET  /api/desk/:id/queue       → JSON: paginated queue rows
 *   POST /api/desk/:id/refresh     → trigger live CourtListener search
 *   POST /webhook/courtlistener    → receive push notifications
 *   GET  /api/audit                → Phase 0 audit report (JSON)
 *   GET  /api/desk/:id/nos-audit   → list non-matching NOS rows in a desk
 */

import { DESKS, getDeskById } from "./desks/config";
import { CourtListenerClient } from "./api/courtlistener";
import { refreshDesk, listQueue, syncOverviewCount } from "./api/ingest";
import { handleWebhook, Env } from "./api/webhook";
import { renderDashboard, renderDeskPage } from "./ui/render";
import { buildAuditReport } from "./api/audit";

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;

    // ── Webhook ─────────────────────────────────────────────────────────────
    if (method === "POST" && path === "/webhook/courtlistener") {
      return handleWebhook(request, env);
    }

    // ── API routes ───────────────────────────────────────────────────────────

    if (path === "/api/desks" && method === "GET") {
      const metas = await env.DB
        .prepare("SELECT * FROM desk_meta")
        .all<{
          desk_id: string;
          last_ingest_at: string | null;
          alert_id: number | null;
          alert_status: string;
          overview_count: number;
        }>();

      const metaMap = Object.fromEntries(
        metas.results.map((m) => [m.desk_id, m])
      );

      return json(
        DESKS.map((d) => ({
          ...d,
          meta: metaMap[d.id] ?? null,
        }))
      );
    }

    const deskQueueMatch = path.match(/^\/api\/desk\/([^/]+)\/queue$/);
    if (deskQueueMatch && method === "GET") {
      const desk = getDeskById(deskQueueMatch[1]);
      if (!desk) return notFound();

      const offset = parseInt(url.searchParams.get("offset") ?? "0", 10);
      const limit = parseInt(
        url.searchParams.get("limit") ?? String(desk.queuePageSize),
        10
      );

      const { rows, total } = await listQueue(env.DB, desk, { limit, offset });
      return json({ desk: desk.id, total, offset, limit, rows });
    }

    const deskRefreshMatch = path.match(/^\/api\/desk\/([^/]+)\/refresh$/);
    if (deskRefreshMatch && method === "POST") {
      const desk = getDeskById(deskRefreshMatch[1]);
      if (!desk) return notFound();

      const cl = new CourtListenerClient(
        env.COURTLISTENER_BASE,
        env.COURTLISTENER_TOKEN
      );

      const result = await refreshDesk(env.DB, desk, cl);
      await syncOverviewCount(env.DB, desk);

      return json({ desk: desk.id, ...result });
    }

    const nosAuditMatch = path.match(/^\/api\/desk\/([^/]+)\/nos-audit$/);
    if (nosAuditMatch && method === "GET") {
      const desk = getDeskById(nosAuditMatch[1]);
      if (!desk) return notFound();

      // Find rows whose NOS code is not in the desk's filter — Phase 2
      const placeholders = desk.nosFilter.map(() => "?").join(",");
      const rows = await env.DB
        .prepare(
          `SELECT id, case_number, case_name, court, nos_code, date_filed
             FROM ${desk.queueTable}
            WHERE nos_code NOT IN (${placeholders})
            ORDER BY date_filed DESC`
        )
        .bind(...desk.nosFilter)
        .all();

      return json({
        desk: desk.id,
        nosFilter: desk.nosFilter,
        nonMatchingCount: rows.results.length,
        nonMatchingRows: rows.results,
        recommendation:
          rows.results.length > 0
            ? "These rows were ingested before the NOS filter was enforced. " +
              "Review each and either mark as 'dismissed-wrong-nos' or delete after " +
              "confirming no letter workflow has started on them."
            : "No non-matching rows found.",
      });
    }

    if (path === "/api/audit" && method === "GET") {
      const cl = new CourtListenerClient(
        env.COURTLISTENER_BASE,
        env.COURTLISTENER_TOKEN
      );
      const report = await buildAuditReport(env.DB, cl);
      return json(report);
    }

    // ── UI routes ────────────────────────────────────────────────────────────

    if (path === "/" || path === "") {
      const metas = await env.DB
        .prepare("SELECT * FROM desk_meta")
        .all<{
          desk_id: string;
          last_ingest_at: string | null;
          alert_id: number | null;
          alert_status: string;
          overview_count: number;
        }>();

      const metaMap = Object.fromEntries(
        metas.results.map((m) => [m.desk_id, m])
      );

      return html(renderDashboard(DESKS, metaMap));
    }

    const deskPageMatch = path.match(/^\/desk\/([^/]+)$/);
    if (deskPageMatch) {
      const desk = getDeskById(deskPageMatch[1]);
      if (!desk) return notFound();

      const offset = parseInt(url.searchParams.get("offset") ?? "0", 10);
      const { rows, total } = await listQueue(env.DB, desk, {
        offset,
        limit: desk.queuePageSize,
      });

      const meta = await env.DB
        .prepare("SELECT * FROM desk_meta WHERE desk_id = ?")
        .bind(desk.id)
        .first<{
          last_ingest_at: string | null;
          alert_status: string;
          overview_count: number;
        }>();

      // Phase 2 count consistency: always read live count
      const liveCount = await syncOverviewCount(env.DB, desk);

      return html(renderDeskPage(desk, rows, total, liveCount, offset, meta));
    }

    return notFound();
  },
};

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

function html(body: string, status = 200): Response {
  return new Response(body, {
    status,
    headers: { "Content-Type": "text/html; charset=utf-8" },
  });
}

function notFound(): Response {
  return new Response("Not found", { status: 404 });
}
