"""
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word of phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just a dictionary words.

EXAMPLE:
Input: "Tact Coa"
Output: True (permutations: "taco cat", "atco cta" etc.)
"""

# Solution 1: use a dictionary
def is_permutation_of_palindrome(phrase: str) -> bool:
    odd_count: int = 0
    table: list[int] = [0] * 26

    for char in phrase:
        idx = get_ascii_value(char)
        if idx != -1:
            table[idx] += 1
            if table[idx] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1

    return odd_count == 1

def get_ascii_value(char: str) -> int:
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a')
    return -1


# Solution 2: using bit vector
def is_palindrome_permutation(s: str) -> bool:
    bit_vector: int = 0

    for c in s:
        x: int = get_ascii_value(c)
        if x != -1:
            mask: int = 1 << x

            if bit_vector & mask == 0:
                bit_vector |= mask
            else:
                bit_vector &= ~mask

    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)

def check_exactly_one_bit_set(bit_vector: int) -> bool:
    return (bit_vector & (bit_vector - 1)) == 0

if __name__ == '__main__':
    assert is_permutation_of_palindrome("Tact Coa") is True
    assert is_permutation_of_palindrome("abca") is False
    assert is_permutation_of_palindrome("Ab Bac") is True

    assert is_palindrome_permutation("Tact Coa") is True
    assert is_palindrome_permutation("abca") is False

