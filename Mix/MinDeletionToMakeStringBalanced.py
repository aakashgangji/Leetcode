"""You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
"""
class Solution:
  # Same as 926. Flip String to Monotone Increasing
  def minimumDeletions(self, s: str) -> int:
    dp = 0  # the number of characters to be deleted to make subso far balanced
    countB = 0

    for c in s:
      if c == 'a':
        # 1. Delete 'a'.
        # 2. Keep 'a' and delete the previous 'b's.
        dp = min(dp + 1, countB)
      else:
        countB += 1

    return dp
s=Solution()
print(s.minimumDeletions("aababbab"))  # 2
print(s.minimumDeletions("bbaaaaabb"))  # 2