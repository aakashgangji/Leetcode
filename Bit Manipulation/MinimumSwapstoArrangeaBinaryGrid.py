"""Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1
"""
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = [0] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    count[i] += 1
                else:
                    break

        swaps = 0
        for i in range(n):
            target = n - 1 - i
            j = i
            while j < n and count[j] < target:
                j += 1
            if j == n:
                return -1
            while j > i:
                count[j], count[j - 1] = count[j - 1], count[j]
                j -= 1
                swaps += 1

        return swaps
# Example usage:
solution = Solution()
print(solution.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))  # Output: 3
print(solution.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))  # Output: -1
print(solution.minSwaps([[1,0,0],[1,1,0],[1,1,1]]))  # Output: 0    
