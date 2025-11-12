"""
You are given a cyclic array nums and an integer k.
Partition nums into at most k subarrays. As nums is cyclic, these subarrays may wrap around from the end of the array back to the beginning.
The range of a subarray is the difference between its maximum and minimum values. The score of a partition is the sum of subarray ranges.
Return the maximum possible score among all cyclic partitions.
Example 1:
Input: nums = [1,2,3,3], k = 2
Output: 3
Explanation:
Partition nums into [2, 3] and [3, 1] (wrapped around).
The range of [2, 3] is max(2, 3) - min(2, 3) = 3 - 2 = 1.
The range of [3, 1] is max(3, 1) - min(3, 1) = 3 - 1 = 2.
The score is 1 + 2 = 3.
Example 2:
Input: nums = [1,2,3,3], k = 1
Output: 2
Explanation:
Partition nums into [1, 2, 3, 3].
The range of [1, 2, 3, 3] is max(1, 2, 3, 3) - min(1, 2, 3, 3) = 3 - 1 = 2.
The score is 2.
Example 3:
Input: nums = [1,2,3,3], k = 4
Output: 3
Explanation:
Identical to Example 1, we partition nums into [2, 3] and [3, 1]. Note that nums may be partitioned into fewer than k subarrays.
"""
from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = nums * 2  # Duplicate the array to handle cyclic nature
        dp = [[float('-inf')] * (k + 1) for _ in range(2 * n + 1)]
        dp[0][0] = 0
        
        for i in range(1, 2 * n + 1):
            current_max = float('-inf')
            current_min = float('inf')
            for j in range(i, 0, -1):
                current_max = max(current_max, nums[j - 1])
                current_min = min(current_min, nums[j - 1])
                range_value = current_max - current_min
                for p in range(1, k + 1):
                    if dp[j - 1][p - 1] != float('-inf'):
                        dp[i][p] = max(dp[i][p], dp[j - 1][p - 1] + range_value)
        
        max_score = float('-inf')
        for i in range(n, 2 * n + 1):
            for p in range(1, k + 1):
                max_score = max(max_score, dp[i][p])
        
        return max_score