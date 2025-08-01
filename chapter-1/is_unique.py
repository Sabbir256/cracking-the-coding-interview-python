"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

# Solution 1: using a list to track seen characters
def is_unique(s: str) -> bool:
    if len(s) > 128:
        return False

    char_set: list[bool] = [False] * 128
    for char in s:
        idx = ord(char)
        if char_set[idx]:
            return False
        char_set[idx] = True

    return True

# Solution 2: using a bit vector
def is_unique_chars(s: str) -> bool:
    checker: int = 0
    for char in s:
        idx = ord(char) - ord('a')
        if (checker & (1 << idx)) > 0:
            return False
        checker |= (1 << idx)

    return True

if __name__ == "__main__":
    assert is_unique("abcde") is True
    assert is_unique("hello") is False

    assert is_unique_chars("abcde") is True
    assert is_unique_chars("hello") is False
