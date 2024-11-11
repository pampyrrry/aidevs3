import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()

aidevs_key = os.getenv("AIDEVS_KEY")
aidevs_url = os.getenv("URL_REPORT")
task = os.getenv("TASK_S01E05")
url = os.getenv("URL_DATA")
url_data = f"{url}{aidevs_key}/cenzura.txt"
cenzura = requests.get(url_data)
print(cenzura.text)

# ollama3 from Cloudflare
data = {
        "q":cenzura.text
        }
url_lama3 = os.getenv("URL_LAMA3")
print(url3)
response_lama = requests.post(url_lama3, data=data)
lama = response_lama.json()
answer = (lama[0]["response"]["response"])
print(answer)
data = {
        "task":task,
        "apikey": aidevs_key,
        "answer": answer
        }
aidevs = requests.post(aidevs_url, json.dumps(data))
print(aidevs.text)
