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
        minheap=[-i for i in nums]
        heapq.heapify(minheap)

        while k>0:
            val=heapq.heappop(minheap)
            val=(-val)
            k-=1
        return (val)



nums= [3,2,1,5,6,4]
k = 2
sol=Solution()
print(sol.findKthLargest(nums,k))