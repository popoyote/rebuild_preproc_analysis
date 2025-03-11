import os
from for_pdfdoc import define_type
from token_stop_lemm import (
    process_file
)


def process_folder(folder_path):
    """Обрабатывает все файлы в папке."""

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Обрабатываем только файлы (игнорируем папки)
        if os.path.isfile(file_path):
            # Обрабатываем файл
            files_text = define_type(file_path)
            process_file(files_text)


folder_path = "pdf_word"  # Укажите путь к папке с файлами
process_folder(folder_path)
