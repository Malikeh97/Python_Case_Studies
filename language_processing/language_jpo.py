from collections import Counter
text = "This is my test text. We're keeping this text short to keep things manageable"

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

text = read_book("./Books/Books_EngFr/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_word_fast(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique)
print(sum(counts))
