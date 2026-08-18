import requests

from core.config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL, LLM_TIMEOUT_SECONDS


class LLMClientError(RuntimeError):
    """A recoverable configuration or provider failure."""


class LLMClient:
    def __init__(self):
        self.api_key = DEEPSEEK_API_KEY
        self.url = f"{DEEPSEEK_BASE_URL.rstrip('/')}/chat/completions"

    def chat(self, system_prompt, user_message):
        if not self.api_key:
            raise LLMClientError("DEEPSEEK_API_KEY is not configured. Add it to .env before chatting.")

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        data = {"model": DEEPSEEK_MODEL, "messages": messages}

        try:
            response = requests.post(self.url, headers=headers, json=data, timeout=LLM_TIMEOUT_SECONDS)
            response.raise_for_status()
            content = response.json()["choices"][0]["message"]["content"]
        except (requests.RequestException, KeyError, IndexError, TypeError, ValueError) as exc:
            raise LLMClientError("The language-model provider did not return a usable reply.") from exc

        if not isinstance(content, str) or not content.strip():
            raise LLMClientError("The language-model provider returned an empty reply.")
        return content.strip()
