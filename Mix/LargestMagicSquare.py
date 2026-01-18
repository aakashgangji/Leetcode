"""A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

Example 1:


Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
Example 2:


Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2
"""
class Solution:
  def largestMagicSquare(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    # prefixRow[i][j] := the sum of the first j numbers in the i-th row
    prefixRow = [[0] * (n + 1) for _ in range(m)]
    # prefixCol[i][j] := the sum of the first j numbers in the i-th column
    prefixCol = [[0] * (m + 1) for _ in range(n)]

    for i in range(m):
      for j in range(n):
        prefixRow[i][j + 1] = prefixRow[i][j] + grid[i][j]
        prefixCol[j][i + 1] = prefixCol[j][i] + grid[i][j]

    def isMagicSquare(i: int, j: int, k: int) -> bool:
      """Returns True if grid[i..i + k)[j..j + k) is a magic square."""
      diag, antiDiag = 0, 0
      for d in range(k):
        diag += grid[i + d][j + d]
        antiDiag += grid[i + d][j + k - 1 - d]
      if diag != antiDiag:
        return False
      for d in range(k):
        if self._getSum(prefixRow, i + d, j, j + k - 1) != diag:
          return False
        if self._getSum(prefixCol, j + d, i, i + k - 1) != diag:
          return False
      return True

    def containsMagicSquare(k: int) -> bool:
      """Returns True if the grid contains any magic square of size k x k."""
      for i in range(m - k + 1):
        for j in range(n - k + 1):
          if isMagicSquare(i, j, k):
            return True
      return False

    for k in range(min(m, n), 1, -1):
      if containsMagicSquare(k):
        return k

    return 1

  def _getSum(self, prefix: list[list[int]], i: int, l: int, r: int) -> int:
    """Returns sum(grid[i][l..r]) or sum(grid[l..r][i])."""
    return prefix[i][r + 1] - prefix[i][l]
S=Solution()
print(S.largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))  # expect 3
print(S.largestMagicSquare([[5,1,3,1],[9,3,3,1],[1,3,3,8]]))  # expect 2