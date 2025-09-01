"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
    
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                low, high = j + 1, n - 1
                
                while low < high:
                    total = nums[i] + nums[j] + nums[low] + nums[high]
                    
                    if total < target:
                        low += 1
                    elif total > target:
                        high -= 1
                    else:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        
                        # Skip duplicates for the third number
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        # Skip duplicates for the fourth number
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        
                        low += 1
                        high -= 1
        
        return result
