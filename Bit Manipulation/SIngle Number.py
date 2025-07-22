# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears only once.
# You must implement a solution with 
# O(n)
# O(n) runtime complexity and use only 
# O (1)
# O(1) extra space.
# Exaple 1:
# Input: nums = [3,2,3]
# Output: 2
# Example 2:
# Input: nums = [7,6,6,7,8]
# Output: 8
from typing import List
def singleNumber(self, nums: List[int]) -> int:
    res=0
    for n in nums:
        res=n^res
    return res

nums = [7,6,6,7,8]
print(singleNumber(None,nums))