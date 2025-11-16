"""
Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
"""
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total_count = 0  
        consecutive_ones = 0  
        for char in s:
            if char == "1":
                consecutive_ones += 1
                total_count += consecutive_ones
            else:
                consecutive_ones = 0
        return total_count % MOD