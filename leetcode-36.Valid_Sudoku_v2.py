'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
https://leetcode.com/problems/valid-sudoku/    
'''
from typing import List

def isValidSudoku(self, board: List[List[str]]) -> bool:
    row, col, blo = set(), set(), set()
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                row_key = (r, board[r][c])  # producing sets of row-index & value-number
                col_key = (c, board[r][c]) # producing sets of row-index & value-number
                # producing sets of row-index & value-number for blocks 0,0 (upper left), 0,1 (upper-middle), 0,2 (upper-right)
                blo_key = (r//3, c//3, board[r][c])
                if ((row_key in row) or (col_key in col) or (blo_key in blo)):
                    return False
                row.add(row_key)
                col.add(col_key)
                blo.add(blo_key)
    print("column-index and value: ",sorted(col))
    print("row-index and value: ", sorted(row))
    print("block-index and value (0, 0 = upper-left): ", sorted(blo))
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
