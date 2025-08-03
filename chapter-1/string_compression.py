"""
1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
"""

def compress(s: str) -> str:
    final_length: int = count_compression(s)
    if final_length >= len(s):
        return s;

    compressed: list[str] = list()
    count: int = 0
    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i])
            compressed.append(str(count))
            count = 0

    return ''.join(compressed)

def count_compression(s: str) -> int:
    length: int = 0
    count: int = 0

    for i in range(len(s)):
        count += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            length += 1 + len(str(count))
            count = 0

    return length

if __name__ == '__main__':
    assert compress('aabccccaaa') == 'a2b1c4a3'
    assert compress('abcd') == 'abcd'
