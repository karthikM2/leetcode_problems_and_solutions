'''Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_count = window_count = 0
        for i in range(len(s)):
            if s[i] in vowels:
                window_count += 1
            if i >= k and s[i-k] in vowels:
                window_count -=1
            max_count = max(max_count,window_count)
        return (max_count)
