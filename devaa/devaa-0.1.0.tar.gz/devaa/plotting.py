import matplotlib.pyplot as plt

def plot_words(words_counts, n=10):
    """Plot a bar chart of word counts."""
    top_n_words = words_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("word")
    plt.ylabel("Count")
    return fig
