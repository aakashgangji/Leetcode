"""
You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2
Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
"""
class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    ans = 0
    maxZero = (-1 + math.sqrt(1 + 4 * len(s))) // 2
    for zero in range(int(maxZero) + 1):
      lastInvalidPos = -1
      count = [0, 0]
      l = 0
      for r, c in enumerate(s):
        count[int(c)] += 1
        while l < r:
          if s[l] == '0' and count[0] > zero:
            count[0] -= 1  # Remove an extra '0'.
            lastInvalidPos = l
            l += 1
          elif s[l] == '1' and count[1] - 1 >= zero * zero:
            count[1] -= 1  # Remove an extra '1'.
            l += 1
          else:
            break  # Cannot remove more characters.
        if count[0] == zero and count[1] >= zero * zero:
            ans += l - lastInvalidPos
    return ans