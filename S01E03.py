from downloadFile import DownloadFile
from openFile import OpenFile
from openAI import OpenAIAssistant
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

aidevs_key = os.getenv("AIDEVS_KEY")
aidevs_url = os.getenv("URL_TAKS_03_REPORT")
url: str = os.getenv("URL_TASK_03_FILE")
url_to_file = f"{url}{aidevs_key}/json.txt"
openAI = OpenAIAssistant()

getFile = DownloadFile(url_to_file)
path_to_file = getFile.download_as_one_file()
print(path_to_file)

openFile = OpenFile(path_to_file)
file = openFile.open()

file["apikey"] = aidevs_key
print(file["apikey"])

for item in file["test-data"]:
    question = item["question"].split("+")
    l = lambda a , b: a + b
    item["answer"] = l(int(question[0]), int(question[1]))
    if "test" in item:
        item["test"]["a"] = openAI.chat(sys_content = "Answer as briefly as possible. Always respond in English", prompt=item["test"]["q"])
data_to_aidevs = {
        "task": "JSON",
        "apikey": aidevs_key,
        "answer": file
        }

to_aidevs = requests.post(url=aidevs_url, data=json.dumps(data_to_aidevs))
print(json.loads(to_aidevs.text))
