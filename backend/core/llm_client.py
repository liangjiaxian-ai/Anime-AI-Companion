import requests

from core.config import DEEPSEEK_API_KEY


class LLMClient:


    def __init__(self):

        self.api_key = DEEPSEEK_API_KEY

        self.url = "https://api.deepseek.com/chat/completions"



    def chat(
            self,
            system_prompt,
            user_message
            ):


        messages=[
            {
                "role":"system",
                "content":system_prompt
            },

            {
                "role":"user",
                "content":user_message
            }
        ]


        headers = {

            "Authorization":
            f"Bearer {self.api_key}",

            "Content-Type":
            "application/json"

        }


        data = {

            "model":"deepseek-chat",

            "messages":messages

        }


        response = requests.post(

            self.url,

            headers=headers,

            json=data

        )


        result = response.json()


        return result["choices"][0]["message"]["content"]