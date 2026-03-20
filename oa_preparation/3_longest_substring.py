"""
Given a string s, find the length of the longest without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

Mental trigger: Longest/shortest substring -> sliding window
"""

def lengthOfLongestSubstring(s):
    char_set = set()
    l = 0
    max_len = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        max_len = max(max_len, r-l+1)
    
    return max_len