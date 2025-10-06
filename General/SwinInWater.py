"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.
You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = [i for i in range(n * n)]
        rank = [1] * (n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        edges = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(n):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n:
                        edges.append((max(grid[i][j], grid[x][y]), i * n + j, x * n + y))

        edges.sort()
        for weight, u, v in edges:
            union(u, v)
            if find(0) == find(n * n - 1):
                return weight
        return 0