import csv
import os
import requests
from urllib.parse import urlparse
import pandas as pd
import multiprocessing as mp


def download_image(url, save_dir, filename):
    """Скачивает изображение по указанному URL и сохраняет его в заданную папку."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        filepath = os.path.join(save_dir, filename)
        
        # Сохраняем изображение
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Изображение сохранено: {filepath}")
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")

def download_images_from_csv(csv_file, save_dir):

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = pd.read_csv(file)
        print(reader)
        
        for idx, url in enumerate(reader['image_url']):
            download_image(url, save_dir, f"{idx}.png")

if __name__ == "__main__":
    dir = "metadata"
    processes = [None] * 4
    for idx, csv_file in enumerate(os.listdir(dir)):
        save_dir = csv_file.split('.')[0]
        os.makedirs(f"data/{save_dir}", exist_ok=True)
        processes[idx] = mp.Process(target=download_images_from_csv, args=(f"{dir}/{save_dir}.csv", f"data/{save_dir}"))
        processes[idx].start()
        
    for process in processes:
        process.join()

    print("All processes are complete.")
