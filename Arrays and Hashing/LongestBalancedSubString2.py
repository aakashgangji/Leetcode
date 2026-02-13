"""You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "aabcc"

Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

Constraints:

1 <= s.length <= 105

s contains only the characters 'a', 'b', and 'c'.
"""
class Solution:
    def longestBalanced(self, s: str) -> int:
        if not s: 
            return 0
        
        max_len = 0
        
        # Scenario 1: Exactly 1 distinct character
        curr_len = 1
        max_len = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
                
        # Scenario 2: Exactly 2 distinct characters
        def get_longest_for_two(c1, c2, exclude_c):
            best = 0
            diff = 0
            # Maps difference to the first time we saw it
            seen = {0: -1} 
            
            for i, char in enumerate(s):
                if char == exclude_c:
                    # Reset the segment if we see the excluded character
                    diff = 0
                    seen = {0: i}
                else:
                    if char == c1:
                        diff += 1
                    elif char == c2:
                        diff -= 1
                        
                    if diff in seen:
                        best = max(best, i - seen[diff])
                    else:
                        seen[diff] = i
            return best
            
        max_len = max(max_len, get_longest_for_two('a', 'b', 'c'))
        max_len = max(max_len, get_longest_for_two('a', 'c', 'b'))
        max_len = max(max_len, get_longest_for_two('b', 'c', 'a'))
        
        # Scenario 3: Exactly 3 distinct characters
        diff_ab = 0
        diff_ac = 0
        # Maps state tuple (diff_ab, diff_ac) to the first time we saw it
        seen_3 = {(0, 0): -1}
        
        for i, char in enumerate(s):
            if char == 'a':
                diff_ab += 1
                diff_ac += 1
            elif char == 'b':
                diff_ab -= 1
            elif char == 'c':
                diff_ac -= 1
                
            state = (diff_ab, diff_ac)
            if state in seen_3:
                max_len = max(max_len, i - seen_3[state])
            else:
                seen_3[state] = i
                
        return max_len