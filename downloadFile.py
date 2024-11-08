import os
import requests

class DownloadFile:
    def __init__(self, url: str):
        app_directory = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(app_directory, "downloads")
        os.makedirs(folder_path, exist_ok=True)
        
        self.url = url
        self.filename = url.split("/")[-1]  # Wyciąganie nazwy pliku z URL
        self.local_filename = os.path.join(folder_path, self.filename)  # Ścieżka do zapisu pliku

    def download_as_one_file(self):
        if not os.path.exists(self.local_filename):
            print("Plik nie istnieje, rozpoczynam pobieranie...")

            with requests.get(self.url, stream=True) as response:
                response.raise_for_status()
                with open(self.local_filename, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
            print(f"Pobrano i zapisano plik jako {self.local_filename}")
        else:
            print("Plik już istnieje, pomijam pobieranie.")

    def download_chunks_file(self, chunk_size: int = 8192):
        chunk_number = 1

        with requests.get(self.url, stream=True) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    # Tworzymy unikalną nazwę pliku dla każdego "chunka"
                    chunk_filename = os.path.join("downloads", f"chunk_{chunk_number}_{self.filename}")
                    with open(chunk_filename, "wb") as file:
                        file.write(chunk)
                    print(f"Pobrano i zapisano {chunk_filename}")
                    chunk_number += 1
