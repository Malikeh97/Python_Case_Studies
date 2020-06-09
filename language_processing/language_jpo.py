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

print(count_word_fast(text))
print(count_word(text) == count_word_fast(text))
