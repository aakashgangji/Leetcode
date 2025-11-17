"""
You are given an integer array nums.

Choose three elements a, b, and c from nums at distinct indices such that the value of the expression a + b - c is maximized.

Return an integer denoting the maximum possible value of this expression.

 

Example 1:

Input: nums = [1,4,2,5]

Output: 8

Explanation:

We can choose a = 4, b = 5, and c = 1. The expression value is 4 + 5 - 1 = 8, which is the maximum possible.

Example 2:

Input: nums = [-2,0,5,-2,4]

Output: 11

Explanation:

We can choose a = 5, b = 4, and c = -2. The expression value is 5 + 4 - (-2) = 11, which is the maximum possible.©leetcode
"""
from typing import List
from typing import List

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        max1 = max2 = float('-inf')
        min1 = float('inf')
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
            if num < min1:
                min1 = num
        
        if len(nums) < 3:
            return None  
        n = len(nums)
        result = float('-inf')
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    value = nums[i] + nums[j] - nums[k]
                    result = max(result, value)
        return result


    
Solution=Solution()
print(Solution.maximizeExpressionOfThree([1,4,2,5]))
print(Solution.maximizeExpressionOfThree([-2,0,5,-2,4]))