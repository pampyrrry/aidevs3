import requests
import os
from bs4 import BeautifulSoup
from openAI import OpenAIAssistant

url = os.getenv("URL_TASK_01")
username: str = "tester"
password: str = "574e112a"
system:str = "Na otrzymane pytanie odpowiedz najkrócej jak to możliwe. Nie używaj znaków interpunkcji, ani nie odpowiadaj pełnym zdaniem. Przykład: [pytanie]: W którym roku wybuchła II wojna światowa? [odpowiedź]: 1939 "

# GET
session = requests.Session()
response = session.get(url)

# BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
question = soup.find(id="human-question")
question = question.text.split(':')

# OpenAI
assistant = OpenAIAssistant()
response = assistant.chat(sys_content= str(system), prompt=str(question))
print(response)

data = {
        "username": username,
        "password": password,
        "answer": int(response)
        }

# POST
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": url
}
post_response = session.post(url, data=data, headers=headers)
print(data)
if post_response.status_code == 200:
    print("Odpowiedź serwera:", post_response.text)
else:
    print("Błąd podczas wysyłania formularza:", post_response.status_code)
