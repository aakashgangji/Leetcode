"""
You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
"""
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        sorted_window = SortedList()
        n = len(nums)
        dp = [1] + [0] * n
        prefix_sum = [1] + [0] * n
        left = 1
        for right in range(1, n + 1):
            sorted_window.add(nums[right - 1])
            while sorted_window[-1] - sorted_window[0] > k:
                sorted_window.remove(nums[left - 1])
                left += 1
            if left >= 2:
                dp[right] = (prefix_sum[right - 1] - prefix_sum[left - 2] + MOD) % MOD
            else:
                dp[right] = prefix_sum[right - 1] % MOD
            prefix_sum[right] = (prefix_sum[right - 1] + dp[right]) % MOD
        return dp[n]