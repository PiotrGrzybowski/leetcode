def roman_to_integer(number: str) -> int:
    """Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M."""
    digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    previous = 0
    result = 0
    for digit in reversed(number):
        value = digits[digit]
        if value >= previous:
            result += value
        else:
            result -= value
        previous = value
    return result


if __name__ == "__main__":
    assert roman_to_integer("III") == 3
    assert roman_to_integer("LVIII") == 58
    assert roman_to_integer("MCMXCIV") == 1994
