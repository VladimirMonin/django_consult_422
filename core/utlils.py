import os
from mistralai import Mistral
# from django.conf import settings  # Правильный способ импорта настроек Django
from prompts import MISTRAL_REVIEW_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MISTRAL_MODEL = os.getenv('MISTRAL_MODEL')

REVIEW = "Всё классно! Но кажется от Бородоча немного несло спиртом. Хотя ему можно простить, он же Бро. В целом рекомендую, если вас это не смущает"

PROMT = MISTRAL_REVIEW_PROMPT.format(review_text=REVIEW)

# Инициализация клиента
client = Mistral(api_key=MISTRAL_API_KEY)

chat_response = client.chat.complete(
    model=MISTRAL_MODEL,
    messages=[
        {
            "role": "user", 
            "content": PROMT
        }
    ]
)
print(chat_response.choices[0].message.content)