"""
1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place)
"""

def replace_spaces(s: str, true_length: int) -> str:
    chars: list = list(s)
    space_count: int  = chars[:true_length].count(' ')

    # for i in range(true_length):
    #     if chars[i] == ' ':
    #         space_count += 1

    index = true_length + space_count * 2
    if index < len(chars):
        chars = chars[:index] # eliminating extra white spaces

    for i in range(true_length - 1, 0, -1):
        if chars[i] == ' ':
            chars[index - 3: index] = '%20'
            index -= 3
        else:
            chars[index - 1] = chars[i]
            index -= 1

    return "".join(chars)

if __name__ == '__main__':
    res: str = replace_spaces('Mr John Smith       ', 13)
    print(res)
    assert res == "Mr%20John%20Smith"

