/* ============================================================
   Newark Law Offices — analytics loader (PHASE 12/13)

   HOW TO TURN ON (pick one or both; no code change needed elsewhere):
   1) GA4  — set GA4_ID below to your Measurement ID (looks like "G-XXXXXXX").
   2) Cloudflare Web Analytics — set CF_BEACON_TOKEN to your beacon token.

   Until an ID is filled in, this file is INERT (loads nothing, tracks
   nothing) — no fake IDs ship. analytics-events.js already routes the
   conversion events (phone_click, consult_cta_click, lead_form_submit,
   guide_download_click, text_click) to gtag once GA4 is loaded here.

   Recommended GA4 "key events" (mark these as conversions in GA4 UI):
     phone_click, consult_cta_click, lead_form_submit, guide_download_click
   ============================================================ */
(function () {
  'use strict';

  // ---- FILL THESE IN ----
  var GA4_ID = '';            // e.g. 'G-XXXXXXXXXX'
  var CF_BEACON_TOKEN = '';   // e.g. 'a1b2c3...' from Cloudflare Web Analytics
  // ------------------------

  // GA4 (gtag.js)
  if (GA4_ID && /^G-[A-Z0-9]+$/.test(GA4_ID)) {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    // anonymize_ip + no ad signals — appropriate for a law firm's visitors
    window.gtag('config', GA4_ID, {
      anonymize_ip: true,
      allow_google_signals: false
    });
  }

  // Cloudflare Web Analytics (cookieless) — optional, complementary to GA4
  if (CF_BEACON_TOKEN) {
    var c = document.createElement('script');
    c.defer = true;
    c.src = 'https://static.cloudflareinsights.com/beacon.min.js';
    c.setAttribute('data-cf-beacon', '{"token":"' + CF_BEACON_TOKEN + '"}');
    document.head.appendChild(c);
  }
})();
