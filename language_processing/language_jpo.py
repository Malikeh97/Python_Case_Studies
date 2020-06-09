from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

text = "This is my test text. We're keeping this text short to keep things manageable"
book_dir = "./Books"
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

def count_word(text):
    word_counts = {}
    text = text.lower()
    skips = [".", ",", ";", ":", '"', "'"]
    for ch in skips:
        text = text.replace(ch, "")

    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def count_word_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", '"', "'"]
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts

# print(count_word_fast(text))
# print(count_word(text) == count_word_fast(text))
# print(count_word(text) is count_word_fast(text))

def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

for language in os.listdir(book_dir):
    if language == ".DS_Store":
        continue
    for author in os.listdir(book_dir + "/" + language):
        if author == ".DS_Store":
            continue
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            if title == ".DS_Store":
                continue
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            text_book = read_book(inputfile)
            word_counts = count_word_fast(text_book)
            (num_unique, counts) = word_stats(word_counts)
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

plt.figure(figsize = (10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")
plt.show()
