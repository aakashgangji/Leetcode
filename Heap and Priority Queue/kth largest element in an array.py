"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k
        def quickselect(l,r):
            pivot,p=nums[r],l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            if p>k:
                return quickselect(l,p-1)
            if p<k:
                return quickselect(p+1,r)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)



nums= [3,2,1,5,6,4]
k = 2
sol=Solution()
print(sol.findKthLargest(nums,k))