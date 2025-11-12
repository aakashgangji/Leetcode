"""
You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1. ​​​​​​​
Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.©leetcode
"""
from typing import List
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        def get_cost_and_score(value):
            if value == 0:
                return 0, 0
            elif value == 1:
                return 1, 1
            elif value == 2:
                return 1, 2
        
        cost, score = get_cost_and_score(grid[0][0])
        if cost <= k:
            dp[0][0][cost] = score
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for c in range(k + 1):
                    if i > 0 and dp[i - 1][j][c] != -1:
                        new_cost, new_score = get_cost_and_score(grid[i][j])
                        total_cost = c + new_cost
                        if total_cost <= k:
                            dp[i][j][total_cost] = max(dp[i][j][total_cost], dp[i - 1][j][c] + new_score)
                    if j > 0 and dp[i][j - 1][c] != -1:
                        new_cost, new_score = get_cost_and_score(grid[i][j])
                        total_cost = c + new_cost
                        if total_cost <= k:
                            dp[i][j][total_cost] = max(dp[i][j][total_cost], dp[i][j - 1][c] + new_score)
        
        max_score = max(dp[m - 1][n - 1])
        return max_score if max_score != -1 else -1

sol=Solution()
print(sol.maxPathScore([[0,1,2],[2,1,0],[1,0,0]], 2))
print(sol.maxPathScore([[0,2,2],[2,1,0],[1,0,0]], 1))
print(sol.maxPathScore([[1,2,1],[2,1,2],[1,2,1]], 4))
print(sol.maxPathScore([[0,1],[2,0]], 1))
print(sol.maxPathScore([[0,1],[1,2]], 1))