"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])  # grid has m rows and n columns
        dp = [[0]* n for _ in range(m)]  # Create a matrix to store the minimum path sums
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    # Starting cell: only option is to start here
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    # First row: can only come from the left
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    # First column: can only come from above
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    # For any other cell, take the min path sum from the left or above
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]  # Answer: minimal path sum to the bottom-right cell
grid = [[1,3,1],[1,5,1],[4,2,1]]
sol=Solution()
print(sol.minPathSum(grid))