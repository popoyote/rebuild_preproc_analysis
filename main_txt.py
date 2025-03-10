# main.py
import for_text
import token_stop_lemm
from visualisation import (
    plot_token_comparison,
    plot_lemmatization_comparison,
    plot_entities_comparison,
)

# Чтение текста
text = for_text.read_text("txt/pedagogika.txt")

# Токенизация
spacy_tokens = token_stop_lemm.tokenize_with_spacy(text)
nltk_tokens = token_stop_lemm.tokenize_with_nltk(text)

# Удаление стоп-слов
spacy_cleaned = token_stop_lemm.remove_stopwords_spacy(spacy_tokens)
nltk_cleaned = token_stop_lemm.remove_stopwords_nltk(nltk_tokens)

# Лемматизация
spacy_lemmas = token_stop_lemm.lemmatize_with_spacy(spacy_cleaned)
nltk_lemmas = token_stop_lemm.lemmatize_with_nltk(nltk_cleaned)

# Извлечение сущностей
spacy_entities = token_stop_lemm.extract_entities_spacy(text)
nltk_entities = token_stop_lemm.extract_entities_nltk(text)

# Визуализация
plot_token_comparison(spacy_tokens, nltk_tokens, spacy_cleaned, nltk_cleaned)
plot_lemmatization_comparison(spacy_lemmas, nltk_lemmas)
plot_entities_comparison(spacy_entities, nltk_entities)

# Вывод результатов
print("Токены (spaCy):", spacy_tokens[:10])
print("Токены (NLTK):", nltk_tokens[:10])
print("Токены без стоп-слов (spaCy):", spacy_cleaned[:10])
print("Токены без стоп-слов (NLTK):", nltk_cleaned[:10])
print("Леммы (spaCy):", spacy_lemmas[:10])
print("Леммы (NLTK):", nltk_lemmas[:10])
print("Сущности (spaCy):", spacy_entities[:5])
print("Сущности (NLTK):", nltk_entities[:5])
