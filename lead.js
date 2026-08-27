/* ============================================================
   Newark Law Offices — shared lead form handler
   Posts the lead form to the Cloudflare Worker. Shows success
   ONLY on a confirmed 2xx response. Never claims delivery on failure.
   ============================================================ */

(function () {
  'use strict';

  var ENDPOINT = 'https://site-chatbots.robert-bb6.workers.dev/lead';

  var form = document.getElementById('leadForm');
  var success = document.getElementById('formSuccess');
  if (!form || !success) return;

  var source = form.getAttribute('data-source') || 'unknown';
  var button = form.querySelector('button[type="submit"]');
  var originalLabel = button ? button.textContent : 'Submit for Review';

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

  function pick(data, keys) {
    for (var i = 0; i < keys.length; i++) {
      var value = data[keys[i]];
      if (value && String(value).trim()) return String(value).trim();
    }
    return '';
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    failure.style.display = 'none';
    success.style.display = 'none';
    if (button) {
      button.disabled = true;
      button.textContent = 'Submitting\u2026';
    }

    var data = {};
    new FormData(form).forEach(function (value, key) {
      data[key] = value;
    });

    // Honeypot — bots fill this, humans never see it. Fail closed without sending.
    if (data.website) {
      success.style.display = 'block';
      form.style.display = 'none';
      if (button) {
        button.disabled = false;
        button.textContent = originalLabel;
      }
      return;
    }

    data.name = pick(data, ['name', 'Name', 'full_name', 'fullName']);
    data.email = pick(data, ['email', 'Email']);
    data.phone = pick(data, ['phone', 'Phone']);
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
          button.textContent = originalLabel;
        }
      });
  });
})();
