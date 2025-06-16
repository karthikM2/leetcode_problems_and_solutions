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

def maxVowels(s: str, k: int) -> int:
    existing_char = set()
    left = 0; start = 0; max_length = 0 
    for i,right in enumerate(range(len(s))):
        print(i);print('in for loop')
        while s[right] in existing_char:
            print('in while loop')
            existing_char.remove(s[left])
            left += 1
        if s[right] in ['a','e','i','o','u']:
            existing_char.add(s[right])
        if right - left + 1 > max_length : 
            max_length = right -left + 1
            start = left

    return(max_length)
        
result = maxVowels("abciiidef", 3)  # Output: 3
print(result)