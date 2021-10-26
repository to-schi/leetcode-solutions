from collections import defaultdict
from random import randint
from typing import List
class Solution:
        def isValidSudoku(self, t_board: List[List[str]]) -> bool:
            cols = defaultdict(set)
            rows = defaultdict(set)
            blocks = defaultdict(set)  # key = (r //3, c //3
            for r in range(9):
                for c in range(9):
                    if t_board[r][c] == ".":
                        continue 
                    if (t_board[r][c] in rows[r] or
                        t_board[r][c] in cols[c] or
                            t_board[r][c] in blocks[r // 3, c // 3]):
                        print(t_board[r][c])
                        return False
                    cols[c].add(t_board[r][c])
                    rows[r].add(t_board[r][c])
                    blocks[(r // 3, c // 3)].add(t_board[r][c])
            print(rows)
            print(cols)
            print(blocks)
            print(rows[0])
            return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        t_board = board.copy()
        for i in range(9):
            for j in range(9):
                t_board[i][j] = randint(0, 9)
                isValidSudoku(1, t_board)
                
    print(solveSudoku(1, [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
