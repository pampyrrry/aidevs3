from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
class OpenAIAssistant:
    def __init__(self):

        self.assistant = OpenAI()

    def chat(self, model: str = "gpt-4o-mini", sys_content: str = "Jesteś pomocnym asystentem", prompt: str = "Cześć"):
        """
        Metoda do interakcji z modelem czatu OpenAI.
        
        :param model: Model, który ma być używany (np. 'gpt-4o-mini').
        :param sys_content: Opis kontentu dla systemu - kim jest asystent.
        :param prompt: Tekst zapytania, na które model ma odpowiedzieć.
        :return: Odpowiedź modelu.
        
        """
        completion = self.assistant.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": sys_content},
        {
            "role": "user",
            "content": prompt
        }])
        return completion.choices[0].message.content
    
    def transcription(self, file_path:str, model: str="whisper-1"):
        transcription = self.assistant.audio.transcriptions.create(
                model=model,
                file=file_path
                )
        return transcription.text
