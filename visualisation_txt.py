import matplotlib.pyplot as plt


def plot_token_comparison(spacy_tokens, nltk_tokens, spacy_cleaned, nltk_cleaned):
    """График сравнения количества токенов до и после удаления стоп-слов."""
    labels = ["spaCy", "NLTK"]
    tokens_before = [len(spacy_tokens), len(nltk_tokens)]
    tokens_after = [len(spacy_cleaned), len(nltk_cleaned)]

    plt.bar(labels, tokens_before, label="До удаления стоп-слов")
    plt.bar(labels, tokens_after, label="После удаления стоп-слов")
    plt.title("Сравнение количества токенов")
    plt.ylabel("Количество токенов")
    plt.legend()
    plt.show()
