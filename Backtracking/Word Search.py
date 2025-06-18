# Word Search
# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
# Example 1:
# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"
# Output: true
# Example 2:
# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"
# Output: false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board), len(board[0])
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        for r in range (rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False