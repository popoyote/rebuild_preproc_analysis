import os
from PIL import Image
from for_pictures import improve_image_quality, extract_text_from_image, convert_to_png
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

# Путь к папке с изображениями
image_folder = "picture"

# Создаем папку для результатов, если её нет
output_folder = "processed_images"
os.makedirs(output_folder, exist_ok=True)

def process_images_in_folder(folder):
    """Обрабатывает все изображения в папке."""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        png_path = convert_to_png(file_path)
        improved_path = improve_image_quality(png_path)
        return extract_text_from_image(improved_path)


# Обработка всех изображений в папке
process_images_in_folder(image_folder)