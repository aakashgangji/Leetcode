"""
You are given an integer array nums.

A subarray of nums is called stable if it contains no inversions, i.e., there is no pair of indices i < j such that nums[i] > nums[j].

You are also given a 2D integer array queries of length q, where each queries[i] = [li, ri] represents a query. For each query [li, ri], compute the number of stable subarrays that lie entirely within the segment nums[li..ri].

Return an integer array ans of length q, where ans[i] is the answer to the ith query.​​​​​​​​​​​​​​

Note:

A single element subarray is considered stable.
 

Example 1:

Input: nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]

Output: [2,3,4]

Explanation:​​​​​

For queries[0] = [0, 1], the subarray is [nums[0], nums[1]] = [3, 1].
The stable subarrays are [3] and [1]. The total number of stable subarrays is 2.
For queries[1] = [1, 2], the subarray is [nums[1], nums[2]] = [1, 2].
The stable subarrays are [1], [2], and [1, 2]. The total number of stable subarrays is 3.
For queries[2] = [0, 2], the subarray is [nums[0], nums[1], nums[2]] = [3, 1, 2].
The stable subarrays are [3], [1], [2], and [1, 2]. The total number of stable subarrays is 4.
Thus, ans = [2, 3, 4].

Example 2:

Input: nums = [2,2], queries = [[0,1],[0,0]]

Output: [3,1]

Explanation:

For queries[0] = [0, 1], the subarray is [nums[0], nums[1]] = [2, 2].
The stable subarrays are [2], [2], and [2, 2]. The total number of stable subarrays is 3.
For queries[1] = [0, 0], the subarray is [nums[0]] = [2].
The stable subarray is [2]. The total number of stable subarrays is 1.
Thus, ans = [3, 1].©leetcode
"""
from typing import List
import bisect

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Find runs: [start, end] inclusive
        runs = []
        i = 0
        while i < n:
            start = i
            while i + 1 < n and nums[i] <= nums[i + 1]:
                i += 1
            runs.append((start, i))
            i += 1
        
        m = len(runs)
        prefix = [0] * (m + 1)
        for i in range(m):
            length = runs[i][1] - runs[i][0] + 1
            prefix[i + 1] = prefix[i] + length * (length + 1) // 2
        
        run_starts = [r[0] for r in runs]
        run_ends = [r[1] for r in runs]
        
        ans = []
        for l, r in queries:
            # Find run index containing l
            idx_l = bisect.bisect_right(run_starts, l) - 1
            # Find run index containing r
            idx_r = bisect.bisect_left(run_ends, r)
            
            if idx_l > idx_r:
                idx_r = idx_l
            
            total = 0
            if idx_l == idx_r:
                # Single run
                start_run, end_run = runs[idx_l]
                start = max(l, start_run)
                end = min(r, end_run)
                length = end - start + 1
                total = length * (length + 1) // 2
            else:
                # Partial left run
                start_left, end_left = runs[idx_l]
                start = max(l, start_left)
                end = min(r, end_left)
                length_left = end - start + 1
                total += length_left * (length_left + 1) // 2
                
                # Partial right run
                start_right, end_right = runs[idx_r]
                start = max(l, start_right)
                end = min(r, end_right)
                length_right = end - start + 1
                total += length_right * (length_right + 1) // 2
                
                # Full runs in between
                if idx_l + 1 <= idx_r - 1:
                    total += prefix[idx_r] - prefix[idx_l + 1]
            
            ans.append(total)
        
        return ans
# Example usage:
sol = Solution()
print(sol.countStableSubarrays([3, 1, 2], [[0, 1], [1, 2], [0, 2]]))  # Output: [2, 3, 4]
print(sol.countStableSubarrays([2, 2], [[0, 1], [0, 0]]))        # Output: [3