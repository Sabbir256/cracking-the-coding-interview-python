"""
1.5 One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if the are one edit (or zero edits) away.

EXAMPLE:
pale,   ple -> True
pales,  pale -> True
pale,   bale -> True
pale,   bae -> False
"""

def one_edit_away(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s2) + 1 == len(s1):
        return one_edit_insert(s2, s1)

    return False

def one_edit_replace(s1: str, s2: str) -> bool:
    flag: bool = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if flag:
                return False
            flag = True

    return True

def one_edit_insert(s1: str, s2: str) -> bool:
    index_s1: int = 0
    index_s2: int = 0

    while index_s2 < len(s2) and index_s1 < len(s1):
        if s1[index_s1] != s2[index_s2]:
            if index_s1 != index_s2: # only for first mismatch they are equal
                return False
        else:
            index_s1 +=1
        index_s2 += 1

    return True


# Alternate solution
def one_away(first: str, second: str) -> bool:
    if abs(len(first) - len(second)) > 1:
        return False

    s1: str = first if len(first) < len(second) else second # shorter string
    s2: str = second if len(first) < len(second) else first # longer string

    index1: int = 0
    index2: int = 0
    flag: bool = False

    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if flag:
                return False
            flag = True

            if index1 == index2:
                index1 += 1 # On replace, move shorter pointer
        else:
            index1 += 1
        index2 += 1

    return True

if __name__ == '__main__':
    assert one_edit_away('pale', 'bale') is True
    assert one_edit_away('abcd', 'mncd') is False
    assert one_edit_away('pales', 'pale') is True
    assert one_edit_away('pale', 'ple') is True

    assert one_away('pale', 'bale') is True
    assert one_away('abcd', 'mncd') is False
    assert one_away('pales', 'pale') is True
    assert one_away('pale', 'bae') is False
