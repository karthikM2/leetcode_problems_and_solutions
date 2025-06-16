#Problem: Find the length of the longest substring without repeating characters.
#Input: s = "abcabcbb"
#Output: 3 (substring: "abc")

'''This is a variable size sliding window problem. '''
def length_of_longest_substring(s):
    existing_chars = set()
    left = 0
    max_length = 0
    start = 0  # To track the start of the longest substring
    
    for right in range(len(s)):
        while s[right] in existing_chars:
            existing_chars.remove(s[left])
            left += 1
        existing_chars.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
    print(max_length)
    print(s[start:start + max_length])

length_of_longest_substring("abcdefabcbb")

 