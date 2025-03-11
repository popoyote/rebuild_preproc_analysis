import os
from for_pdfdoc import define_type
from token_stop_lemm import (
    process_file
)


def process_folder(folder_path, output_folder):
    """Обрабатывает все файлы в папке."""
    # Создаем папку для результатов, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Обрабатываем только файлы (игнорируем папки)
        if os.path.isfile(file_path):
            # Обрабатываем файл
            files_text = define_type(file_path)
            process_file(files_text)


folder_path = "pdf_word"  # Укажите путь к папке с файлами
output_folder = "results"  # Папка для сохранения результатов
process_folder(folder_path, output_folder)
