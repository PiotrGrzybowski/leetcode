def sub_str(haystack: str, needle: str) -> int:
    """Finds index of first occurrence of needle in haystack."""
    if not needle:
        return 0
    index = 0
    while index <= len(haystack) - len(needle):
        i = 0
        while i < len(needle) and haystack[index + i] == needle[i]:
            i += 1

        if i == len(needle):
            return index

        index += 1
    return -1


if __name__ == '__main__':
    assert sub_str("hello", "") == 0
    assert sub_str("hello", "ll") == 2
    assert sub_str("hello", "lls") == -1
    assert sub_str("aaaa", "aaa") == 0
