from typing import List
def solveNQueens(n: int) -> List[List[str]]:
    res=[]
    cols=set()
    posdiagonal=set()
    negdiagonal=set()
    board=[["."]*n for i in range(n)]

    def backtrack(r):
        if r==n:
            copy=["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in cols or (r-c) in negdiagonal or (r+c) in posdiagonal:
                continue
            cols.add(c)
            posdiagonal.add(r+c)
            negdiagonal.add(r-c)
            board[r][c]="Q"

            backtrack(r+1)

            cols.remove(c)
            posdiagonal.remove(r+c)
            negdiagonal.remove(r-c)
            board[r][c]="."

    backtrack(0)
    return res


n=4
print(solveNQueens(n))