"""Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
Example 3:

Input: s = "1"
Output: 0
"""
class Solution:
  def numSteps(self, s: str) -> int:
    ans = 0
    chars = list(s)

    # All the trailing 0s can be popped by 1 step.
    while chars[-1] == '0':
      chars.pop()
      ans += 1

    if ''.join(chars) == '1':
      return ans

    # `s` is now odd, so add 1 to `s` and cost 1 step.
    # All the 1s will become 0s and can be popped by 1 step.
    # All the 0s will become 1s and can be popped by 2 steps (adding 1 then
    # dividing by 2).
    return ans + 1 + sum(1 if c == '1' else 2 for c in chars)