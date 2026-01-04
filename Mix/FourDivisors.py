"""Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
"""
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            # Skip small and perfect squares (they cannot have exactly 4 divisors)
            r = int(n ** 0.5)
            if n <= 4 or r * r == n:
                continue
            count = 2          # 1 and n
            s = 1 + n
            for d in range(2, r + 1):
                if n % d == 0:
                    count += 2
                    s += d + n // d
                    if count > 4:
                        break
            if count == 4:
                ans += s
        return ans
