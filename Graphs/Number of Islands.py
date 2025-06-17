# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        islands=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q=deque()
            grid[r][c]="0"
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr, dc in directions:
                    nr,nc=dr+row,dc+col
                    if(nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]=="0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]="0"
    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands