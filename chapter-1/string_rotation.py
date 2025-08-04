"""
1.9 String Rotation: Assuem you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of erbottlewat").
"""

def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) > 0 and len(s1) == len(s2):
        s1s1: str = s1 + s1
        return is_substring(s1s1, s2)
    return False

def is_substring(first: str, second: str) -> bool:
    # we can also search by sliding window
    return second in first

if __name__ == '__main__':
    assert is_rotation("waterbottle", "erbottlewat") is True
    assert is_rotation('helloworld', 'worldhello') is True
    assert is_rotation('abcd', 'cab') is False
