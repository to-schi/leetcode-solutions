def validSudoku(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == ".":
                board[i][j] = None
    blocks = [[board[0][0:3], board[1][0:3], board[2][0:3]], [board[0][3:6], board[1][3:6], board[2][3:6]],
              [board[0][6:9], board[1][6:9], board[2][6:9]], [board[3][0:3], board[4][0:3], board[5][0:3]],
              [board[3][3:6], board[4][3:6], board[5][3:6]], [board[3][6:9], board[4][6:9], board[5][6:9]],
              [board[6][0:3], board[7][0:3], board[8][0:3]], [board[6][3:6], board[7][3:6], board[8][3:6]],
              [board[6][6:9], board[7][6:9], board[8][6:9]]]
    blocklist = []
    for b in range(0,9):
        blocklist.append(blocks[b])
        new = [x for x in blocklist if x is not None]
        print(new)
        for i in range(0, 9):
                if blocklist[i] == ".":
                    blocklist[i] = None
        for nums in blocklist[b]:
            if [x for x in blocks[b] if x is not None].count(nums) > 1:
                return False
    for r in range (0, 9):   
        #print([x for x in board[r] if x is not None])
        for nums in board[r]:
            if [x for x in board[r] if x != None].count(nums) > 1:
                return False
    
    for r in range(0,9):
        for c in renge(0,9):
            for nums in board[r]:
            if [x for x in board[r] if x != None].count(nums) > 1:
                return False
            for nums in board[c]
        
        #a = [x for x in col if x != None].count(nums)
        #print(a)
        col = board[r][c]

        if [x for x in col if x != None].count(nums) > 1:
            return False
    return True
    
print(validSudoku([["6", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
