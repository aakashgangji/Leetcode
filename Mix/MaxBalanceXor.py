"""
Given an integer array nums, return the length of the longest subarray that has a bitwise XOR of zero and contains an equal number of even and odd numbers. If no such subarray exists, return 0.

 

Example 1:

Input: nums = [3,1,3,2,0]

Output: 4

Explanation:

The subarray [1, 3, 2, 0] has bitwise XOR 1 XOR 3 XOR 2 XOR 0 = 0 and contains 2 even and 2 odd numbers.

Example 2:

Input: nums = [3,2,8,5,4,14,9,15]

Output: 8

Explanation:

The whole array has bitwise XOR 0 and contains 4 even and 4 odd numbers.

Example 3:

Input: nums = [0]

Output: 0

Explanation:

No non-empty subarray satisfies both conditions.
"""
class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        seen = dict()
        # State: (xor_sum, even_minus_odd): first_index_seen
        seen[(0, 0)] = -1  # base case
        xor_sum = 0
        even_minus_odd = 0
        res = 0
        
        for i, num in enumerate(nums):
            xor_sum ^= num
            if num % 2 == 0:
                even_minus_odd += 1
            else:
                even_minus_odd -= 1
            key = (xor_sum, even_minus_odd)
            if key in seen:
                res = max(res, i - seen[key])
            else:
                seen[key] = i
        return res
