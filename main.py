import sys

from stats import count_characters, count_words, sort_characters


def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    char_dict = count_characters(text)
    char_list = sort_characters(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")


main()
