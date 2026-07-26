/* ============================================================
   Newark Law Offices — shared lead form handler
   Posts the lead form to the Cloudflare Worker. Shows success
   ONLY on a confirmed 2xx response. Never claims delivery on failure.
   ============================================================ */

(function () {
  'use strict';

  // TODO: set this to the live Worker route before deploying.
  var ENDPOINT = 'https://site-chatbots.robert-bb6.workers.dev/lead';

  var form = document.getElementById('leadForm');
  var success = document.getElementById('formSuccess');
  if (!form || !success) return;

  var source = form.getAttribute('data-source') || 'unknown';
  var button = form.querySelector('button[type="submit"]');

  // Failure message element, created once and reused.
  var failure = document.createElement('div');
  failure.className = 'form-error';
  failure.setAttribute('role', 'alert');
  failure.style.display = 'none';
  success.parentNode.insertBefore(failure, success.nextSibling);

  function showFailure() {
    failure.innerHTML =
      'We could not submit this form. Please call ' +
      '<a href="tel:+18662307236">(866) 230-7236</a> ' +
      'so your matter is not delayed.';
    failure.style.display = 'block';
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    failure.style.display = 'none';
    success.style.display = 'none';
    if (button) {
      button.disabled = true;
      button.textContent = 'Submitting\u2026';
    }

    // Honeypot — bots fill this, humans never see it
    var hp = form.querySelector('input[name="website"]');
    var data = {};
    new FormData(form).forEach(function (value, key) {
      data[key] = value;
    });
    data.source = source;
    data.page = window.location.pathname;
    data.submitted_at = new Date().toISOString();

    fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        success.style.display = 'block';
        form.style.display = 'none';
      })
      .catch(function () {
        showFailure();
      })
      .then(function () {
        if (button) {
          button.disabled = false;
          button.textContent = 'Submit for Review';
        }
      });
  });
})();
