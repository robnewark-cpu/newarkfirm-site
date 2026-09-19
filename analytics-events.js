/* ============================================================
   Newark Law Offices — conversion event tracking (PHASE 13)
   Lightweight, privacy-respecting. Fires custom events that any
   analytics provider (Cloudflare Web Analytics, GA4, Plausible)
   can consume. No PII is sent here — only event category/label.
   Wire a provider by implementing window.nloTrack(name, props).
   ============================================================ */
(function () {
  'use strict';

  function track(name, props) {
    try {
      // Preferred: a provider hook the site owner defines.
      if (typeof window.nloTrack === 'function') {
        window.nloTrack(name, props || {});
        return;
      }
      // GA4 gtag, if present.
      if (typeof window.gtag === 'function') {
        window.gtag('event', name, props || {});
        return;
      }
      // Fallback: dataLayer push (GTM) or a no-op console in dev.
      (window.dataLayer = window.dataLayer || []).push(
        Object.assign({ event: name }, props || {}));
    } catch (e) { /* never break the page for analytics */ }
  }

  var practice = (document.body.getAttribute('data-practice') || '').trim();
  var page = window.location.pathname;

  // Phone-click tracking (any tel: link)
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var cta = a.getAttribute('data-cta') || '';

    if (href.indexOf('tel:') === 0) {
      track('phone_click', { page: page, practice: practice, cta: cta || 'phone' });
    } else if (href.indexOf('sms:') === 0) {
      track('text_click', { page: page, practice: practice });
    } else if (cta === 'consult') {
      track('consult_cta_click', { page: page, practice: practice });
    } else if (cta === 'download') {
      track('guide_download_click', {
        page: page, practice: practice,
        guide: a.getAttribute('data-guide') || ''
      });
    }
  });

  // Form submission tracking — listen on the shared lead form.
  var form = document.getElementById('leadForm');
  if (form) {
    form.addEventListener('submit', function () {
      track('lead_form_submit', {
        page: page,
        practice: practice,
        source: form.getAttribute('data-source') || 'unknown',
        matter: (form.querySelector('[name="matter"]') || {}).value || ''
      });
    });
  }
})();
