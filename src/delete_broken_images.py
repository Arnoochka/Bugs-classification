import os
from PIL import Image

def is_image_broken(image_path):
    """Проверяет, является ли изображение битым."""
    try:
        with Image.open(image_path) as img:
            img.verify()
        return False
    except (IOError, SyntaxError):
        return True

def delete_broken_images(folder_path):
    """Удаляет битые изображения из указанной папки."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_image_broken(file_path):
                print(f"Удаляю битое изображение: {file_path}")
                os.remove(file_path)

if __name__ == "__main__":
    for folder in os.listdir('data'):
        if os.path.isdir(f"data/{folder}"):
            delete_broken_images(f"data/{folder}")
            print("Проверка завершена.")
        else:
            print("Указанная папка не существует.")