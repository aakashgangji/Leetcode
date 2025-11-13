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
from typing import Tuple
from typing import List

class SegmentTree:
    def __init__(self, data: List[int], func):
        self.n = len(data)
        self.func = func
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = func(self.tree[i << 1], self.tree[(i << 1) | 1])
        
    def query(self, left: int, right: int) -> int:
        result = None
        left += self.size
        right += self.size
        while left <= right:
            if left & 1:
                result = self.tree[left] if result is None else self.func(result, self.tree[left])
                left += 1
            if not (right & 1):
                result = self.tree[right] if result is None else self.func(result, self.tree[right])
                right -= 1
            left >>= 1
            right >>= 1
        return result


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums2 = nums * 2  
        min_tree = SegmentTree(nums2, min)
        max_tree = SegmentTree(nums2, max)
        
        def range_min_max(l: int, r: int):
            return min_tree.query(l, r), max_tree.query(l, r)
        
        result = 0
        
        for start in range(n):
            
            dp = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
            dp[0][0] = 0
            
            for i in range(n):
                for parts in range(k):
                    if dp[i][parts] == float('-inf'):
                        continue
                    for length in range(1, n - i + 1):
                        end = start + i + length - 1
                        seg_min, seg_max = range_min_max(end - length + 1, end)
                        score = seg_max - seg_min
                        if dp[i][parts] + score > dp[i + length][parts + 1]:
                            dp[i + length][parts + 1] = dp[i][parts] + score
            
            for parts in range(1, k + 1):
                result = max(result, dp[n][parts])
        
        return result
sol=Solution()
print(sol.maximumScore([1,2,3,3],2))  # Output:3
print(sol.maximumScore([1,2,3,3],1))  # Output:2
print(sol.maximumScore([1,2,3,3],4))  # Output:3
print(sol.maximumScore([508882051,438704141,690816744,309083087,255949298,171618882,154132662,694584660,708267128,789067611,875112610,45802814,400568685,401850803,332220238,792292312,273160690,899127162,844501372,69916474,13058775,336901690,119923752,36817842,735793463,62311579,226559477,136468391,239577457,431985794,89905730,289900658,996939364,665092513,600645243,979117571,156930576,949027160,906228412,955927135,437541819,823746051,40587905,849012331,543157336,228197669,181715590,511971910],18))
    
