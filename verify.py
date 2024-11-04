from dotenv import load_dotenv
import os
import requests
import json
from typing import List

load_dotenv() # wczytanie zmiennych z .env

api_key: str = os.getenv("AIDEVS_KEY")
task: str = "POLIGON"
task_url: str = "https://poligon.aidevs.pl/dane.txt"
answer_url: str = "https://poligon.aidevs.pl/verify"

response = requests.get(task_url)
response_txt: str  = response.text
split: List[str] = response_txt.split('\n')

answer_data: dict[str, List[str]] = {
        "task": task,
        "apikey": api_key,
        "answer": split[0:2]
        }

answer = requests.post(answer_url, json=answer_data)
answer = answer.json()

print(answer)





