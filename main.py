from stats import count_words


def get_book_text(fp):
    with open(fp) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    words = count_words(text)
    print(f"Found {words} total words")


main()
