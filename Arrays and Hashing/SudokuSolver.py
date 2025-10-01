"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle using optimized backtracking with MRV and constraint sets.
        Modify the board in-place.
        """

        # Precompute constraints for rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Track empty cells
        empty_cells = []

        # Initialize constraints and empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(val)

        def get_candidates(r: int, c: int) -> List[str]:
            """Return possible candidates for cell (r, c)"""
            box_index = (r // 3) * 3 + (c // 3)
            return [str(n) for n in range(1, 10) if str(n) not in rows[r] and str(n) not in cols[c] and str(n) not in boxes[box_index]]

        def solve() -> bool:
            if not empty_cells:
                return True

            # Sort the empty cells by number of candidates (MRV heuristic)
            empty_cells.sort(key=lambda x: len(get_candidates(x[0], x[1])))
            r, c = empty_cells.pop(0)
            box_index = (r // 3) * 3 + (c // 3)

            for num in get_candidates(r, c):
                # Place num
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

                if solve():
                    return True

                # Undo move
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_index].remove(num)

            # Backtrack
            empty_cells.insert(0, (r, c))
            return False

        solve()
