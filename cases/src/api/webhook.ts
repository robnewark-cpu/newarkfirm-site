/**
 * CourtListener webhook handler.
 *
 * CourtListener POSTs an alert payload to /webhook/courtlistener when a
 * new docket matches a saved alert. This handler validates the payload,
 * identifies the target desk by alert ID, enforces the NOS filter, and
 * writes to D1.
 *
 * Phase 1 fix: stalled desks had either no registered alert or a paused one.
 * Once re-registered (see config.ts), this handler will receive their pushes.
 */

import { DESKS } from "../desks/config";
import { CourtListenerClient, CLDocket } from "./courtlistener";
import { ingestDocket } from "./ingest";

export interface Env {
  DB: D1Database;
  QUEUE_KV: KVNamespace;
  COURTLISTENER_TOKEN: string;
  COURTLISTENER_BASE: string;
  WEBHOOK_SECRET?: string;
}

/** CourtListener alert webhook payload shape. */
interface CLWebhookPayload {
  webhook: {
    event_type: number; // 1 = new docket
    version: number;
    payload: {
      results: CLDocket[];
    };
  };
}

export async function handleWebhook(
  request: Request,
  env: Env
): Promise<Response> {
  // Validate HMAC signature when WEBHOOK_SECRET is configured
  if (env.WEBHOOK_SECRET) {
    const sig = request.headers.get("X-CL-Webhook-Signature") ?? "";
    const body = await request.text();
    const valid = await verifyHmac(env.WEBHOOK_SECRET, body, sig);
    if (!valid) {
      return new Response("Unauthorized", { status: 401 });
    }
    const data = JSON.parse(body) as CLWebhookPayload;
    return await processPayload(data, env);
  }

  const data = (await request.json()) as CLWebhookPayload;
  return await processPayload(data, env);
}

async function processPayload(
  data: CLWebhookPayload,
  env: Env
): Promise<Response> {
  if (!data?.webhook?.payload?.results) {
    return new Response("Bad Request", { status: 400 });
  }

  const cl = new CourtListenerClient(
    env.COURTLISTENER_BASE,
    env.COURTLISTENER_TOKEN
  );

  let totalInserted = 0;
  let totalRejected = 0;

  for (const docket of data.webhook.payload.results) {
    // Identify which desk(s) this docket belongs to by matching NOS codes
    // against all desks. A single webhook push can match multiple desks
    // (e.g. PI overlaps with Trucking/Aviation/Maritime on some NOS codes).
    for (const desk of DESKS) {
      const ok = await ingestDocket(env.DB, desk, docket, desk.courtListenerAlertId, cl);
      if (ok) totalInserted++;
      else totalRejected++;
    }
  }

  return new Response(
    JSON.stringify({ inserted: totalInserted, rejected: totalRejected }),
    { status: 200, headers: { "Content-Type": "application/json" } }
  );
}

async function verifyHmac(
  secret: string,
  body: string,
  signature: string
): Promise<boolean> {
  try {
    const key = await crypto.subtle.importKey(
      "raw",
      new TextEncoder().encode(secret),
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["verify"]
    );
    const sigBytes = hexToBytes(signature);
    const bodyBytes = new TextEncoder().encode(body);
    return await crypto.subtle.verify("HMAC", key, sigBytes, bodyBytes);
  } catch {
    return false;
  }
}

function hexToBytes(hex: string): Uint8Array {
  const bytes = new Uint8Array(hex.length / 2);
  for (let i = 0; i < hex.length; i += 2) {
    bytes[i / 2] = parseInt(hex.slice(i, i + 2), 16);
  }
  return bytes;
}
