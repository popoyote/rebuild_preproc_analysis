# data_extraction.py
import spacy
from natasha import NamesExtractor, MorphVocab

# Загрузка необходимых ресурсов
morph_vocab = MorphVocab()
nlp = spacy.load("ru_core_news_sm")
nlp.max_length = 4_000_000


def read_text(file_path):
    """Чтение текста из файла."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
