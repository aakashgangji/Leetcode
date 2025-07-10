# Islands and Treasure
# Solved 
# You are given a 
# m
# ×
# n
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]
from typing import List
from collections import deque
def islandsAndTreasure(grid: List[List[int]]) -> None:
    ROWS,COLS=len(grid), len(grid[0])
    visit=set()
    q=deque()
    def addcell(r,c):
        if(r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or grid[r][c]==-1):
            return
        visit.add((r,c))
        q.append([r,c])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c]==0:
                visit.add((r,c))
                q.append([r,c])
    
    dist=0
    while q:
        for i in range(len(q)):
            r,c=q.popleft()
            grid[r][c]=dist
            addcell(r+1,c)
            addcell(r-1,c)
            addcell(r,c+1)
            addcell(r,c-1)
        dist+=1
grid= [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]


print(islandsAndTreasure(grid))
print(grid)

