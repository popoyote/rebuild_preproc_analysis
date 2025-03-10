import os
from for_pdfdoc import extract_text_pypdf2, extract_text_docx
from token_stop_lemm import (
    tokenize_with_spacy,
    remove_stopwords_spacy,
    lemmatize_with_spacy,
    extract_entities_spacy,
    tokenize_with_nltk,
    remove_stopwords_nltk,
    lemmatize_with_nltk,
    extract_entities_nltk
)
from visualisation import (
    plot_token_comparison,
    plot_lemmatization_comparison,
    plot_entities_comparison,
)


def process_file(file_path):
    """Обрабатывает файл в зависимости от его расширения."""
    # Получаем расширение файла
    _, file_extension = os.path.splitext(file_path)

    # Приводим расширение к нижнему регистру для унификации
    file_extension = file_extension.lower()

    # Обработка PDF
    if file_extension == ".pdf":
        print(f"Обработка PDF-файла: {file_path}")
        text = extract_text_pypdf2(file_path)

    # Обработка DOCX
    elif file_extension == ".docx":
        print(f"Обработка DOCX-файла: {file_path}")
        text = extract_text_docx(file_path)

    # Неподдерживаемый формат
    else:
        print(f"Неподдерживаемый формат файла: {file_path}")
        return None

    # Общая обработка текста (токенизация, удаление стоп-слов, лемматизация, извлечение сущностей)
    print("Токенизация текста...")
    tokens_spacy = tokenize_with_spacy(text)
    tokens_nltk = tokenize_with_nltk(text)

    print("Удаление стоп-слов...")
    cleaned_tokens_spacy = remove_stopwords_spacy(tokens_spacy)
    cleaned_tokens_nltk = remove_stopwords_nltk(tokens_nltk)

    print("Лемматизация текста...")
    lemmas_spacy = lemmatize_with_spacy(cleaned_tokens_spacy)
    lemmas_nltk = lemmatize_with_nltk(cleaned_tokens_nltk)

    print("Извлечение сущностей...")
    entities_spacy = extract_entities_spacy(text)
    entities_nltk = extract_entities_nltk(text)

    # Визуализация результатов (опционально)
    plot_token_comparison(tokens_spacy, tokens_nltk, cleaned_tokens_spacy, cleaned_tokens_nltk)
    plot_lemmatization_comparison(lemmas_spacy, lemmas_nltk)
    plot_entities_comparison(entities_spacy, entities_nltk)

    # Возвращаем результаты
    return {
        "file_path": file_path,
        "text": text,
        "tokens": tokens_spacy,
        "cleaned_tokens": cleaned_tokens_spacy,
        "lemmas": lemmas_spacy,
        "entities": entities_spacy,
    }


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
            try:
                # Обрабатываем файл
                result = process_file(file_path)

                # Если файл успешно обработан, сохраняем результаты
                if result:
                    output_file = os.path.join(output_folder, f"{filename}_results.txt")
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(f"Файл: {result['file_path']}\n")
                        f.write(f"Текст: {result['text'][:1000]}...\n\n")  # Сохраняем первые 1000 символов
                        f.write(f"Токены: {result['tokens'][:100]}\n\n")
                        f.write(f"Токены без стоп-слов: {result['cleaned_tokens'][:100]}\n\n")
                        f.write(f"Леммы: {result['lemmas'][:100]}\n\n")
                        f.write(f"Сущности: {result['entities'][:20]}\n")
                    print(f"Результаты сохранены в: {output_file}")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_path}: {e}")


# Пример использования
if __name__ == "__main__":
    folder_path = "pdf_word"  # Укажите путь к папке с файлами
    output_folder = "results"  # Папка для сохранения результатов
    process_folder(folder_path, output_folder)