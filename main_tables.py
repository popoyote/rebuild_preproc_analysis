import os
from token_stop_lemm import (
    process_file
)
from for_tables import (
    extract_text_from_table
)

# Путь к папке с изображениями
image_folder = "tables"

# Создаем папку для результатов, если её нет
output_folder = "processed_images"
os.makedirs(output_folder, exist_ok=True)


def process_folder(folder_path):
    """Обрабатывает все файлы в папке."""

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Обрабатываем только файлы (игнорируем папки)
        if os.path.isfile(file_path):
            # Обрабатываем файл
            files_text = extract_text_from_table(file_path)
            print(file_path)
            process_file(files_text)


folder_path = "tables"  # Укажите путь к папке с файлами
process_folder(folder_path)
