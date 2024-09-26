def count_words(c):
    return len(c.split())


def char_freq(c):
    chars = {}
    for char in c.lower():
        if not char.isalpha():
            continue
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars


def sort_on(dict):
    return dict["count"]


def generate_report(path, words, c_freq):
    list_of_dicts = []
    for c in c_freq:
        list_of_dicts.append({"char": c, "count": c_freq[c]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the content")
    for d in list_of_dicts:
        print(f"The '{d['char']}' character was found {d['count']} times")
    print("--- End report ---")


with open("books/frankenstein.txt", "r") as f:
    content = f.read()
    word_count = count_words(content)
    c_freq = char_freq(content)
    generate_report("books/frankenstein.txt", word_count, c_freq)
