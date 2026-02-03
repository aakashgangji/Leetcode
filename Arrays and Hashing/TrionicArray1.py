"""You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

 

Example 1:

Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
Example 2:

Input: nums = [2,1,3]

Output: false

Explanation:

There is no way to pick p and q to form the required three segments.
"""
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        i = 0
        
        # Find the peak of the first increasing sequence
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        # Peak cannot be at the start or end
        if i == 0 or i == n - 1:
            return False
        
        # Find the trough of the decreasing sequence
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        
        # Trough cannot be at the end
        if j == n - 1:
            return False
        
        # Check for the final increasing sequence
        while j + 1 < n and nums[j] < nums[j + 1]:
            j += 1
        
        return j == n - 1