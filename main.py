from stats import count_words, count_letters, sort_letters


def get_book_text(fp):
    with open(fp) as f:
        return f.read()


def print_report(path):
    text = get_book_text(path)
    word_cnt = count_words(text)
    letters = count_letters(text)
    sorted = sort_letters(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_cnt} total words")
    print("--------- Character Count -------")
    for l in sorted:
        if l["char"].isalpha():
            print(f"{l['char']}: {l['num']}")
    print("============= END ===============")


def main():
    print_report("books/frankenstein.txt")


main()
