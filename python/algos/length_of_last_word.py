def length_of_last_word(text: str) -> int:
    """Returns length of last word in text."""
    i = len(text) - 1
    while text[i] == " ":
        i -= 1
    pointer = i
    while i >= 0 and text[i] != " ":
        i -= 1

    return pointer - i


def length_of_last_word_python(text: str) -> int:
    """Returns length of last word in text."""
    return len(text.strip().split(" ")[-1])


if __name__ == "__main__":
    assert length_of_last_word_python("Hello World") == 5
    assert length_of_last_word_python("luffy is still joyboy") == 6
    assert length_of_last_word_python("   fly me   to   the moon  ") == 4
    assert length_of_last_word_python("a") == 1
