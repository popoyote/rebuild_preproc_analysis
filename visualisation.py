# visualisation.py
import matplotlib.pyplot as plt


def plot_token_comparison(spacy_tokens, nltk_tokens, spacy_cleaned, nltk_cleaned):
    """
    График сравнения количества токенов до и после удаления стоп-слов.

    :param spacy_tokens: Токены, полученные с помощью spaCy.
    :param nltk_tokens: Токены, полученные с помощью NLTK.
    :param spacy_cleaned: Токены после удаления стоп-слов (spaCy).
    :param nltk_cleaned: Токены после удаления стоп-слов (NLTK).
    """
    labels = ["spaCy", "NLTK"]
    tokens_before = [len(spacy_tokens), len(nltk_tokens)]
    tokens_after = [len(spacy_cleaned), len(nltk_cleaned)]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, tokens_before, label="До удаления стоп-слов", color="blue", alpha=0.6)
    plt.bar(labels, tokens_after, label="После удаления стоп-слов", color="green", alpha=0.6)
    plt.title("Сравнение количества токенов")
    plt.ylabel("Количество токенов")
    plt.legend()
    plt.show()


def plot_lemmatization_comparison(spacy_lemmas, nltk_lemmas):
    """
    График сравнения количества лемм.

    :param spacy_lemmas: Леммы, полученные с помощью spaCy.
    :param nltk_lemmas: Леммы, полученные с помощью NLTK.
    """
    labels = ["spaCy", "NLTK"]
    lemmas_count = [len(spacy_lemmas), len(nltk_lemmas)]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, lemmas_count, color=["orange", "purple"], alpha=0.6)
    plt.title("Сравнение количества лемм")
    plt.ylabel("Количество лемм")
    plt.show()


def plot_entities_comparison(spacy_entities, nltk_entities):
    """
    График сравнения количества извлеченных сущностей.

    :param spacy_entities: Сущности, извлеченные с помощью spaCy.
    :param nltk_entities: Сущности, извлеченные с помощью NLTK.
    """
    labels = ["spaCy", "NLTK"]
    entities_count = [len(spacy_entities), len(nltk_entities)]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, entities_count, color=["red", "cyan"], alpha=0.6)
    plt.title("Сравнение количества сущностей")
    plt.ylabel("Количество сущностей")
    plt.show()