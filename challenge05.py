def longest_palindrome(text):
    if not text:
        return ""

    pal_start = 0
    pal_length = 1
    length = len(text)

    def expand_window(left, right):
        nonlocal pal_start, pal_length
        while left >= 0 and right < length and text[left] == text[right]:
            if right - left + 1 > pal_length:
                pal_start = left
                pal_length = right - left + 1
            left -= 1
            right += 1

    for i in range(length):
        expand_window(i, i)
        expand_window(i, i + 1)

    return text[pal_start:pal_start + pal_length]


s1 = "babad"
print(longest_palindrome(s1))  

s2 = "forgeeksskeegfor"
print(longest_palindrome(s2)) 

s3 = "abacdfgdcaba"
print(longest_palindrome(s3))  
