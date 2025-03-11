import os
from PIL import Image
from for_pictures import improve_image_quality, extract_text_from_image, convert_to_png
from token_stop_lemm import (
    process_file
)

# Путь к папке с изображениями
image_folder = "picture"

# Создаем папку для результатов, если её нет
output_folder = "processed_images"
os.makedirs(output_folder, exist_ok=True)


def process_images_in_folder(folder):
    """Обрабатывает все изображения в папке."""
    for filename in os.listdir(folder):
        # Полный путь к файлу
        file_path = os.path.join(folder, filename)

        # Конвертируем в PNG, если нужно
        png_path = convert_to_png(file_path)

        # Извлекаем текст
        files_text = extract_text_from_image(png_path)
        print(files_text)
        # Если текст извлечен, обрабатываем его
        if files_text:
            process_file(files_text)
        else:
            print(f"Текст не извлечен из изображения {filename}")


# Обработка всех изображений в папке
process_images_in_folder(image_folder)
