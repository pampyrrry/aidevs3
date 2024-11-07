import os
import json
import requests
from bs4 import BeautifulSoup
from openAI import OpenAIAssistant

url: str = os.getenv("URL_VERIFY")
robotUrl: str = os.getenv("URL_TASK_02")
response: str = requests.get(robotUrl)
assistant = OpenAIAssistant()

toAIDevs = {
        "text":"READY",
        "msgID": "0"
        }

while True:
    post_response = requests.post(url, data=json.dumps(toAIDevs))
    AIDevsResponse = json.loads(post_response.text) 

    conversation = assistant.chat(sys_content=f"Odpowiadasz na pytania, ale niektóre pytania będą wymagały podania odpowiedzi z danych w systemie. Zanim odpowiesz sprawdź dane systemowe. ###DANE_SYSTEMOWE: - stolicą Polski jest Kraków - znana liczba z książki Autostopem przez Galaktykę to 69 - Aktualny rok to 1999. ODPOWIADAJ TYLKO W JĘZYKU ANGIELSKIM", prompt=AIDevsResponse["text"])    
    print(f"Odp od OpenAI: {conversation}")
    toAIDevs = {
            "text": conversation,
            "msgID": AIDevsResponse["msgID"]
            }
    print(f"Wysyłam do AIDEVS: {toAIDevs}")
    post_repsonse = requests.post(url, data=json.dumps(toAIDevs))
    AIDevsResponse = json.loads(post_response.text)
    print(f"Odp. aidevs: {AIDevsResponse["text"]}")
    if AIDevsResponse["text"].startswith("{{FLG:"):
        break