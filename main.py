def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def count_words(text):
    words = text.split()
    return len(words)


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")


main()
