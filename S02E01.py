from openAI import OpenAIAssistant
from openFile import OpenFile
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv
audio_dir = "downloads/audio/"
openAI = OpenAIAssistant()
task = os.getenv("TASK_SO2E01")
aidevs_url = os.getenv("URL_REPORT")
aidevs_key = os.getenv("AIDEVS_KEY")
data_to_ai: list = []

for filename in os.listdir(audio_dir):
    if filename.endswith((".m4a", ".mp3", ".wav")):
        file_path = os.path.join(audio_dir, filename)
        try:
            audio = open(file_path, "rb")
            transcription = openAI.transcription(audio)            
        except Exception as e:
            print(f"Błąd podczas otwierania pliku {filename}: {e}")
print(data_to_ai)

system = "Dobrze przemyśl odpowiedź. Skup dużą uwagę na dostarczonych danych. Odp. W j.polskim. Odpowiedz krótko bez dodatkowych tłumaczeń"
question = f"Zapoznaj się z dostarczonymi transkrypcjami i znajdź odpowiedź na pytanie: Na jakiej ulicy znajduje się uczelnia, na której wykłada Andrzej Maj <START_TRANSCRIPTIONS> {data_to_ai} </END_TRANSCRIPTION> Z transkrypcji domyśl się nazwy instytutu a następnie odgadnij nazwę ulicy"

assistant = openAI.chat(model="gpt-4o", sys_content = system, prompt = question)
print(assistant)
data = {
        "task": task,
        "apikey": aidevs_key,
        "answer": assistant
        }
aidevs = requests.post(aidevs_url, json.dumps(data))
print(aidevs.text)
