from collections import defaultdict
from typing import List
def isValidSudoku(self, board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    blocks = defaultdict(set) # key = (r //3, c //3
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in blocks[r //3, c //3]):
                print(board[r][c])
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            blocks[(r //3, c //3)].add(board[r][c])
    print(rows)
    print(cols)
    print(blocks)
    print(rows[0])
    return True

print(isValidSudoku(1, [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
