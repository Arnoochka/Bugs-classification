import os
from PIL import Image

def validate_images(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Проверка изображения
            except (IOError, SyntaxError):
                print(f"Corrupted image: {file_path}")
                os.remove(file_path)  # Удаление поврежденного изображения


if __name__ == "__main__":
    dataset = "data/not_splitted"
    for dir in os.listdir(dataset):
        validate_images(f"{dataset}/{dir}")
