"""Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array."""
class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
    n = 1 << k
    if len(s) < n:
      return False

    # used[i] := True if i is a substring of `s`
    used = [0] * n

    windowStr = 0 if k == 1 else int(s[0:k - 1], 2)
    for i in range(k - 1, len(s)):
      # Include the s[i].
      windowStr = (windowStr << 1) + int(s[i])
      # Discard the s[i - k].
      windowStr &= n - 1
      used[windowStr] = True

    return all(u for u in used)