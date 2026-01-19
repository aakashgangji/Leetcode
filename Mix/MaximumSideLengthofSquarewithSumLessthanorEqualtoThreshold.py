"""Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
"""
class Solution:
  def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
    m = len(mat)
    n = len(mat[0])
    ans = 0
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
      for j in range(n):
        prefix[i + 1][j + 1] = (mat[i][j] + prefix[i][j + 1] +
                                prefix[i + 1][j] - prefix[i][j])

    def squareSum(r1: int, c1: int, r2: int, c2: int) -> int:
      return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]

    for i in range(m):
      for j in range(n):
        for length in range(ans, min(m - i, n - j)):
          if squareSum(i, j, i + length, j + length) > threshold:
            break
          ans = max(ans, length + 1)

    return ans