"""
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:
Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [2,5,7,8,9,2,3,4,3,1]
Output: 3
Explanation:
The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:
Input: nums = [1,2,3,4,4,4,4,5,6,7]
Output: 2
Explanation:
The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
"""
from typing import List
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        incLen = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                incLen[i] = incLen[i + 1] + 1
        
        def can_find(k: int) -> bool:
            for start in range(n - 2 * k + 1):
                if incLen[start] >= k and incLen[start + k] >= k:
                    return True
            return False
        
        left, right = 1, n // 2
        max_k = 0
        while left <= right:
            mid = (left + right) // 2
            if can_find(mid):
                max_k = mid  # mid is possible, try for a larger k
                left = mid + 1
            else:
                right = mid - 1
        
        return max_k
