def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters_dict = {}
    for char in text.lower():
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict


def sort_by_num(dict):
    return dict["num"]


def sort_characters(characters):
    char_list = []
    for char in characters:
        char_list.append({"char": char, "num": characters[char]})
    char_list.sort(key=sort_by_num, reverse=True)
    return char_list
