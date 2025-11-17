"""
You are given a positive integer n.

For every integer x from 1 to n, we write down the integer obtained by removing all zeros from the decimal representation of x.

Return an integer denoting the number of distinct integers written down.

 

Example 1:

Input: n = 10

Output: 9

Explanation:

The integers we wrote down are 1, 2, 3, 4, 5, 6, 7, 8, 9, 1. There are 9 distinct integers (1, 2, 3, 4, 5, 6, 7, 8, 9).

Example 2:

Input: n = 3

Output: 3

Explanation:

The integers we wrote down are 1, 2, 3. There are 3 distinct integers (1, 2, 3).©leetcode
"""
class Solution:
    def countDistinct(self, n: int) -> int:

        s = str(n)
        L = len(s)
        count = 0
        pow9 = 1
        for i in range(1, L):
            pow9 *= 9
            count += pow9
        has_zero_so_far = False
        for i in range(L):
            d_char = s[i]
            d_val = int(d_char)
            
            if d_val == 0:
                has_zero_so_far = True
                break
                
            remaining_digits = L - 1 - i
            pow9 = 9**remaining_digits
            num_smaller_digits = d_val - 1
            count += num_smaller_digits * pow9
        if not has_zero_so_far:
            count += 1
            
        return count


sol=Solution()
print(sol.countDistinct(10))  # Output: 9
print(sol.countDistinct(3))   # Output: 3

