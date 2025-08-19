# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

from typing import List
def maxProduct(self, nums: List[int]) -> int:
    curmin,curmax=1,1
    res=max(nums)

    for n in nums:
        tmp=curmax*n
        curmax=max(curmax*n,curmin*n,n)
        curmin=min(curmin*n,tmp,n)
        res=max(res,curmax)
    return res

nums=[1,0,4,-6,-2,-1]
print(maxProduct(None,nums))