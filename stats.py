def count_words(text):
    return len(text.split())


def count_letters(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counts = {}
    for letter in alphabet:
        counts[letter] = text.count(letter)
    return counts


def sort_letters(letters):
    sorted = []
    for k, v in letters.items():
        sorted.append({"char": k, "num": v})

    def get_num(item):
        return item["num"]

    sorted.sort(reverse=True, key=get_num)
    return sorted
