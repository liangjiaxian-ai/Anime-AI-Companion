const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const messages = document.querySelector("#messages");
const status = document.querySelector("#status");
const sendButton = document.querySelector("#send-button");
const userIdInput = document.querySelector("#user-id");

userIdInput.value = localStorage.getItem("anime-companion-user-id") || "1";
userIdInput.addEventListener("change", () => localStorage.setItem("anime-companion-user-id", userIdInput.value));

function addMessage(name, content, type) {
  const article = document.createElement("article");
  article.className = `message ${type}-message`;
  const sender = document.createElement("span");
  sender.className = "message-name";
  sender.textContent = name;
  const text = document.createElement("p");
  text.textContent = content;
  article.append(sender, text);
  messages.append(article);
  messages.scrollTop = messages.scrollHeight;
}

function resizeInput() {
  input.style.height = "auto";
  input.style.height = `${Math.min(input.scrollHeight, 120)}px`;
}

async function sendMessage(message) {
  addMessage("你", message, "user");
  input.value = "";
  resizeInput();
  sendButton.disabled = true;
  status.className = "status";
  status.textContent = "星野正在思考…";

  try {
    const response = await fetch("/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: Number(userIdInput.value) || 1, message }),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.detail || "暂时无法连接到服务。");
    addMessage(payload.character || "星野", payload.reply, "assistant");
    status.textContent = "按 Enter 发送，Shift + Enter 换行";
  } catch (error) {
    status.className = "status error";
    status.textContent = error.message || "发送失败，请检查服务和 API 配置。";
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (message) sendMessage(message);
});
input.addEventListener("input", resizeInput);
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});
document.querySelectorAll(".suggestions button").forEach((button) => {
  button.addEventListener("click", () => sendMessage(button.textContent));
});
