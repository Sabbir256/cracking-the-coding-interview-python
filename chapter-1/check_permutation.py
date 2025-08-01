"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

# Solution 1: using sort
def permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


# Solution 2: character counts
def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    letters: list[int] = [0] * 128
    for char in s1:
        letters[ord(char)] += 1

    for char in s2:
        idx = ord(char)
        letters[idx] -= 1
        if letters[idx] < 0:
            return False
    return True


if __name__ == '__main__':
    assert permutation('pga', 'gap') is True
    assert permutation('ab', 'cd') is False
    assert check_permutation('pga', 'gap') is True
    assert check_permutation('ab', 'cd') is False
