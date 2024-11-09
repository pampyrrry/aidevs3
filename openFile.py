import os
import requests
import json
import re

class OpenFile():
    def __init__(self, path_to_file:str):
        self.path_to_file = path_to_file
    
    def open(self) -> str:
        # text file
        try:
            with open(self.path_to_file, 'r') as file:
                data = json.loads(file.read())
                return data
        except FileNotFoundError:
            print(f"Błąd: Plik {self.path_to_file} nie został znaleziony.")
            return ""
        except IOError as e:
            print(f"Błąd we/wy: Nie udało się otworzyć pliku {self.path_to_file}. Szczegóły: {e}")
            return ""

    def open_binary(self) -> bytes:
        # pdf, audio, video file
        try: 
            with open(self.path_to_file, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Błąd: Plik {self.path_to_file} nie został znaleziony.")
            return b""
        except IOError as e:
            print(f"Błąd we/wy: Nie udało się otworzyć pliku {self.path_to_file}. Szczegóły: {e}")
            return b""
    '''
    def split_json_file(self, self.path_to_file, output_dir: str, chunk_size: int = 10):
        self.data = self.open()
        self.data = data.strip()[1:-1]
    '''
