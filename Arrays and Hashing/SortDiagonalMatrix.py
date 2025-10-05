"""
You are given an n x n square matrix of integers grid. Return the matrix such that:
The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
Example 1:
Input: grid = [[1,7,3],[9,8,2],[4,5,6]]
Output: [[8,2,3],[9,6,7],[4,5,1]]
Explanation:
The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:
[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:
[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:
Input: grid = [[0,1],[1,2]]
Output: [[2,1],[1,0]]
Explanation:
The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.
Example 3:
Input: grid = [[1]]
Output: [[1]]
Explanation:
Diagonals with exactly one element are already in order, so no changes are needed.
"""
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # Process diagonals starting from the left edge (column 0)
        # Starting from row n-2 down to row 0
        for start_row in range(n - 2, -1, -1):
            row, col = start_row, 0
            diagonal_values = []
            # Collect all values along the diagonal (moving down-right)
            while row < n and col < n:
                diagonal_values.append(grid[row][col])
                row += 1
                col += 1
            # Sort the diagonal values in ascending order
            diagonal_values.sort()
            # Place sorted values back along the diagonal in descending order
            # (popping from sorted list gives largest values first)
            row, col = start_row, 0
            while row < n and col < n:
                grid[row][col] = diagonal_values.pop()
                row += 1
                col += 1
        # Process diagonals starting from the bottom edge (row n-1)
        # Starting from column n-2 down to column 1
        for start_col in range(n - 2, 0, -1):
            row, col = start_col, n - 1
            diagonal_values = []
            # Collect all values along the diagonal (moving up-left)
            while row >= 0 and col >= 0:
                diagonal_values.append(grid[row][col])
                row -= 1
                col -= 1
            # Sort the diagonal values in ascending order
            diagonal_values.sort()
            # Place sorted values back along the diagonal in descending order
            # (popping from sorted list gives largest values first)
            row, col = start_col, n - 1
            while row >= 0 and col >= 0:
                grid[row][col] = diagonal_values.pop()
                row -= 1
                col -= 1
        return grid