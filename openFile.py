import os
import requests

class OpenFile():
    def __init__(self, path_to_file:str):
        self.path_to_file = path_to_file
    
    def open(self) -> str:
        # text file
        try:
            with open(self.path_to_file, 'r') as file:
                return file.read()
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

