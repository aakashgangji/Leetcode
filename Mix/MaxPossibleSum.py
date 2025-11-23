"""
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.
Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
"""
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        remainder = total_sum % 3
        
        if remainder == 0:
            return total_sum
        
        mod1 = sorted([num for num in nums if num % 3 == 1])
        mod2 = sorted([num for num in nums if num % 3 == 2])
        
        option1 = total_sum - (mod1[0] if mod1 else float('inf'))
        option2 = total_sum - (mod2[0] + mod2[1] if len(mod2) >= 2 else float('inf'))
        
        if remainder == 1:
            return max(total_sum - (mod1[0] if mod1 else float('inf')),
                       total_sum - (mod2[0] + mod2[1] if len(mod2) >= 2 else float('inf')))
        else:  # remainder == 2
            return max(total_sum - (mod2[0] if mod2 else float('inf')),
                       total_sum - (mod1[0] + mod1[1] if len(mod1) >= 2 else float('inf')))