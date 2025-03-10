# text_processing.py
import spacy
from natasha import NamesExtractor, MorphVocab
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymorphy2

# Загрузка необходимых ресурсов
nltk.download("punkt")
nltk.download("stopwords")
nlp = spacy.load("ru_core_news_sm")
nlp.max_length = 4_000_000
morph_vocab = MorphVocab()


def tokenize_with_spacy(text):
    """Токенизация с помощью spaCy."""
    doc = nlp(text)
    return [token.text for token in doc]


def tokenize_with_nltk(text):
    """Токенизация с помощью NLTK."""
    return word_tokenize(text, language="russian")


def remove_stopwords_spacy(tokens):
    """Удаление стоп-слов с помощью spaCy."""
    doc = nlp(" ".join(tokens))
    return [token.text for token in doc if not token.is_stop]


def remove_stopwords_nltk(tokens):
    """Удаление стоп-слов с помощью NLTK."""
    stop_words = set(stopwords.words("russian"))
    return [word for word in tokens if word.isalnum() and word not in stop_words]


def lemmatize_with_spacy(tokens):
    """Лемматизация с помощью spaCy."""
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]


def lemmatize_with_nltk(tokens):
    """Лемматизация с помощью NLTK и pymorphy2."""
    morph = pymorphy2.MorphAnalyzer()
    return [morph.parse(word)[0].normal_form for word in tokens if word.isalnum()]


def extract_entities_spacy(text):
    """Извлечение сущностей с помощью spaCy."""
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]


def extract_entities_nltk(text):
    """Извлечение сущностей с помощью Natasha."""
    extractor = NamesExtractor(morph_vocab)
    entities = []

    # Разделяем текст на части
    text_parts = [text[i:i + 100_000] for i in range(0, len(text), 100_000)]

    # Обрабатываем каждую часть
    for part in text_parts:
        matches = extractor(part)
        entities.extend([{"first": match.fact.first, "last": match.fact.last} for match in matches])

    return entities