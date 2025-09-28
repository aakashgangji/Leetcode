"""
You are given a 2D array queries, where queries[i] is of the form [l, r]. Each queries[i] defines an array of integers nums consisting of elements ranging from l to r, both inclusive.
In one operation, you can:
Select two integers a and b from the array.
Replace them with floor(a / 4) and floor(b / 4).
Your task is to determine the minimum number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.
Example 1:
Input: queries = [[1,2],[2,4]]
Output: 3
Explanation:
For queries[0]:
The initial array is nums = [1, 2].
In the first operation, select nums[0] and nums[1]. The array becomes [0, 0].
The minimum number of operations required is 1.
For queries[1]:
The initial array is nums = [2, 3, 4].
In the first operation, select nums[0] and nums[2]. The array becomes [0, 3, 1].
In the second operation, select nums[1] and nums[2]. The array becomes [0, 0, 0].
The minimum number of operations required is 2.
The output is 1 + 2 = 3.
Example 2:
Input: queries = [[2,6]]
Output: 4
Explanation:
For queries[0]:
The initial array is nums = [2, 3, 4, 5, 6].
In the first operation, select nums[0] and nums[3]. The array becomes [0, 3, 4, 1, 6].
In the second operation, select nums[2] and nums[4]. The array becomes [0, 3, 1, 1, 1].
In the third operation, select nums[1] and nums[2]. The array becomes [0, 0, 0, 1, 1].
In the fourth operation, select nums[3] and nums[4]. The array becomes [0, 0, 0, 0, 0].
The minimum number of operations required is 4.
The output is 4.
"""
import bisect
from typing import List
class Solution:
  def minOperations(self, queries: List[List[int]]) -> int:
    p4 = [1]
    while p4[-1] <= 10**9:
        p4.append(p4[-1] * 4)
        
    prefix_sums = [0] * len(p4)
    for k in range(1, len(p4)):
        count_in_range_k = p4[k] - p4[k-1]
        ops_for_range_k = k * count_in_range_k
        prefix_sums[k] = prefix_sums[k-1] + ops_for_range_k
    
    memo = {}

    def F(n: int) -> int:
        if n == 0:
            return 0
        if n in memo:
            return memo[n]

        K = bisect.bisect_right(p4, n)
        
        sum_full_ranges = prefix_sums[K-1]
        
        count_partial_range = n - p4[K-1] + 1
        sum_partial_range = K * count_partial_range
        
        result = sum_full_ranges + sum_partial_range
        memo[n] = result
        return result

    total_result = 0
    for l, r in queries:
        total_ops_in_range = F(r) - F(l - 1)
        operations_for_query = (total_ops_in_range + 1) // 2
        total_result += operations_for_query
        
    return total_result
  