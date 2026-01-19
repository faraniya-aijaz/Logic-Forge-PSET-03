def find_anagrams(text, pattern):
    result = []
    if len(pattern) > len(text):
        return result

    pattern_count = [0] * 26
    window_count = [0] * 26

    for ch in pattern:
        pattern_count[ord(ch) - ord('a')] += 1

    window_size = len(pattern)

    for i in range(len(text)):
        window_count[ord(text[i]) - ord('a')] += 1

        if i >= window_size:
            window_count[ord(text[i - window_size]) - ord('a')] -= 1

        if window_count == pattern_count:
            result.append(i - window_size + 1)

    return result


s1 = "cbaebabacd"
p1 = "abc"
print(find_anagrams(s1, p1))

s2 = "bacaab"
p2 = "ba"
print(find_anagrams(s2, p2))

s3 = "xyzxyx"
p3 = "xy"
print(find_anagrams(s3, p3))
