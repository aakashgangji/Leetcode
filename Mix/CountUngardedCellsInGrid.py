"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.
Example 1:
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
"""
from typing import List
class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # Initialize grid: 0 = unguarded, 1 = guarded, 2 = guard/wall
        grid = [[0] * n for _ in range(m)]
      
        # Mark guards on the grid
        for row, col in guards:
            grid[row][col] = 2
      
        # Mark walls on the grid
        for row, col in walls:
            grid[row][col] = 2
      
        # Direction vectors: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      
        # For each guard, mark all cells they can see in four directions
        for guard_row, guard_col in guards:
            for delta_row, delta_col in directions:
                current_row, current_col = guard_row, guard_col
              
                # Continue in current direction until hitting boundary or obstacle
                while (0 <= current_row + delta_row < m and 
                       0 <= current_col + delta_col < n and 
                       grid[current_row + delta_row][current_col + delta_col] < 2):
                    current_row += delta_row
                    current_col += delta_col
                    grid[current_row][current_col] = 1  # Mark as guarded
      
        # Count unguarded cells (cells with value 0)
        unguarded_count = sum(cell == 0 for row in grid for cell in row)
      
        return unguarded_count
    
sol=Solution()
print(sol.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))   
print(sol.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]))