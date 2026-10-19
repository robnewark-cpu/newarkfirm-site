/**
 * Embeddable chat widget. Drop this snippet before </body> on each site,
 * changing only the data attributes:
 *
 * <script
 *   src="https://YOUR-CDN-OR-SAME-SITE/widget.js"
 *   data-worker-url="https://your-worker.your-subdomain.workers.dev"
 *   data-site="newarkfirm"
 *   data-name="Newark Law Offices"
 *   data-accent="#0F1B2E"
 *   data-greeting="Hi! I can help point you to the right person here — what brings you by today?"
 * ></script>
 *
 * data-site must match a key in worker.js's SITE_CONFIGS object:
 *   newarkfirm | aegis | mod | vls
 */
(function () {
  const scriptTag = document.currentScript;
  const WORKER_URL = scriptTag.dataset.workerUrl;
  const SITE = scriptTag.dataset.site;
  const NAME = scriptTag.dataset.name || "Chat";
  const ACCENT = scriptTag.dataset.accent || "#1a1a2e";
  const GREETING =
    scriptTag.dataset.greeting || "Hi — what can I help you with today?";

  if (!WORKER_URL || !SITE) {
    console.error("[chat-widget] missing data-worker-url or data-site");
    return;
  }

  const STORAGE_KEY = "chatwidget:" + SITE;
  let history = [];
  try {
    const saved = sessionStorage.getItem(STORAGE_KEY);
    if (saved) history = JSON.parse(saved);
  } catch (e) {}

  // ---------- styles ----------
  const style = document.createElement("style");
  style.textContent = `
    .cw-root { position: fixed; bottom: 20px; right: 20px; z-index: 999999; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .cw-bubble { width: 60px; height: 60px; border-radius: 50%; background: ${ACCENT}; box-shadow: 0 6px 20px rgba(0,0,0,0.25); border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: transform 0.15s ease; }
    .cw-bubble:hover { transform: scale(1.06); }
    .cw-bubble svg { width: 26px; height: 26px; }
    .cw-panel { position: absolute; bottom: 76px; right: 0; width: 340px; max-width: calc(100vw - 40px); height: 460px; max-height: calc(100vh - 140px); background: #fff; border-radius: 14px; box-shadow: 0 12px 40px rgba(0,0,0,0.22); display: none; flex-direction: column; overflow: hidden; border: 1px solid rgba(0,0,0,0.08); }
    .cw-panel.cw-open { display: flex; }
    .cw-header { background: ${ACCENT}; color: #fff; padding: 14px 16px; display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; }
    .cw-header-title { font-size: 14px; font-weight: 600; }
    .cw-header-sub { font-size: 11px; opacity: 0.75; margin-top: 1px; }
    .cw-close { background: none; border: none; color: #fff; opacity: 0.8; cursor: pointer; font-size: 18px; line-height: 1; padding: 4px; }
    .cw-close:hover { opacity: 1; }
    .cw-messages { flex: 1; overflow-y: auto; padding: 14px; display: flex; flex-direction: column; gap: 10px; background: #fafafa; }
    .cw-msg { max-width: 82%; padding: 9px 12px; border-radius: 12px; font-size: 13.5px; line-height: 1.45; white-space: pre-wrap; word-wrap: break-word; }
    .cw-msg.user { align-self: flex-end; background: ${ACCENT}; color: #fff; border-bottom-right-radius: 3px; }
    .cw-msg.bot { align-self: flex-start; background: #fff; color: #222; border: 1px solid #e5e5e5; border-bottom-left-radius: 3px; }
    .cw-msg a { color: inherit; text-decoration: underline; }
    .cw-typing { align-self: flex-start; display: flex; gap: 3px; padding: 10px 12px; }
    .cw-typing span { width: 5px; height: 5px; border-radius: 50%; background: #999; animation: cw-bounce 1.2s infinite ease-in-out; }
    .cw-typing span:nth-child(2) { animation-delay: 0.15s; }
    .cw-typing span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes cw-bounce { 0%, 60%, 100% { transform: translateY(0); opacity: 0.5; } 30% { transform: translateY(-4px); opacity: 1; } }
    .cw-inputrow { border-top: 1px solid #eee; padding: 8px; display: flex; gap: 6px; flex-shrink: 0; background: #fff; }
    .cw-input { flex: 1; border: 1px solid #ddd; border-radius: 20px; padding: 9px 14px; font-size: 13.5px; outline: none; font-family: inherit; }
    .cw-input:focus { border-color: ${ACCENT}; }
    .cw-send { background: ${ACCENT}; border: none; color: #fff; width: 36px; height: 36px; border-radius: 50%; cursor: pointer; flex-shrink: 0; display: flex; align-items: center; justify-content: center; }
    .cw-send:disabled { opacity: 0.5; cursor: default; }
    .cw-disclaimer { font-size: 10px; color: #999; text-align: center; padding: 4px 8px 8px; }
    @media (max-width: 480px) {
      .cw-panel { width: calc(100vw - 32px); right: -4px; }
    }
  `;
  document.head.appendChild(style);

  // ---------- markup ----------
  const root = document.createElement("div");
  root.className = "cw-root";
  root.innerHTML = `
    <div class="cw-panel" id="cw-panel">
      <div class="cw-header">
        <div>
          <div class="cw-header-title">${escapeHtml(NAME)}</div>
          <div class="cw-header-sub">Usually replies instantly</div>
        </div>
        <button class="cw-close" id="cw-close" aria-label="Close chat">&times;</button>
      </div>
      <div class="cw-messages" id="cw-messages"></div>
      <div class="cw-inputrow">
        <input class="cw-input" id="cw-input" type="text" placeholder="Type a message..." />
        <button class="cw-send" id="cw-send" aria-label="Send">
          <svg viewBox="0 0 24 24" fill="none" width="16" height="16"><path d="M3 12l18-9-9 18-2-7-7-2z" stroke="white" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </button>
      </div>
      <div class="cw-disclaimer">AI assistant — for general info only.</div>
    </div>
    <button class="cw-bubble" id="cw-bubble" aria-label="Open chat">
      <svg viewBox="0 0 24 24" fill="none"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" stroke="white" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>
    </button>
  `;
  document.body.appendChild(root);

  const panel = root.querySelector("#cw-panel");
  const bubble = root.querySelector("#cw-bubble");
  const closeBtn = root.querySelector("#cw-close");
  const messagesEl = root.querySelector("#cw-messages");
  const input = root.querySelector("#cw-input");
  const sendBtn = root.querySelector("#cw-send");

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function linkify(text) {
    const escaped = escapeHtml(text);
    return escaped
      .replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>')
      .replace(/([\w.+-]+@[\w-]+\.[\w.-]+)/g, '<a href="mailto:$1">$1</a>');
  }

  function renderMessage(role, text) {
    const div = document.createElement("div");
    div.className = "cw-msg " + (role === "user" ? "user" : "bot");
    div.innerHTML = linkify(text);
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function renderAll() {
    messagesEl.innerHTML = "";
    if (history.length === 0) {
      renderMessage("assistant", GREETING);
    } else {
      history.forEach((m) => renderMessage(m.role, m.content));
    }
  }

  function showTyping() {
    const div = document.createElement("div");
    div.className = "cw-typing";
    div.id = "cw-typing-indicator";
    div.innerHTML = "<span></span><span></span><span></span>";
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  function hideTyping() {
    const el = document.getElementById("cw-typing-indicator");
    if (el) el.remove();
  }

  function persist() {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(history.slice(-20)));
    } catch (e) {}
  }

  async function sendMessage(text) {
    history.push({ role: "user", content: text });
    renderMessage("user", text);
    persist();
    input.value = "";
    sendBtn.disabled = true;
    showTyping();

    try {
      const res = await fetch(WORKER_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ site: SITE, messages: history }),
      });
      const data = await res.json();
      hideTyping();

      if (!res.ok || !data.reply) {
        renderMessage(
          "assistant",
          "Sorry, something went wrong on my end. Please try again, or reach us directly through the contact info on this page."
        );
      } else {
        history.push({ role: "assistant", content: data.reply });
        renderMessage("assistant", data.reply);
        persist();
      }
    } catch (err) {
      hideTyping();
      renderMessage(
        "assistant",
        "I'm having trouble connecting right now. Please try again in a moment."
      );
    } finally {
      sendBtn.disabled = false;
      input.focus();
    }
  }

  bubble.addEventListener("click", () => {
    panel.classList.toggle("cw-open");
    if (panel.classList.contains("cw-open")) {
      if (messagesEl.children.length === 0) renderAll();
      input.focus();
    }
  });
  closeBtn.addEventListener("click", () => panel.classList.remove("cw-open"));

  sendBtn.addEventListener("click", () => {
    const text = input.value.trim();
    if (text) sendMessage(text);
  });
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      const text = input.value.trim();
      if (text) sendMessage(text);
    }
  });
})();
