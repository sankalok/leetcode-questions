class Solution(object):
    def __init__(self):
        self.c = True
        
    def check(self, board):
        for i in board:
            if(i != "." and board.count(i) > 1):
                self.c = False
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(0, len(board)):
            checkR = []
            checkC = []
            for j in range(0, len(board)):
                if board[i][j] in checkR:
                    return False
                if(board[i][j] != "." and board[i][j] not in checkR):
                    checkR.append(board[i][j])
                if board[j][i] in checkC:
                    return False
                if(board[j][i] != "." and board[j][i] not in checkC):
                    checkC.append(board[j][i])
        
        box1 = board[0][0:3] + board[1][0:3] + board[2][0:3]
        box2 = board[0][3:6] + board[1][3:6] + board[2][3:6]
        box3 = board[0][6:9] + board[1][6:9] + board[2][6:9]
        
        box4 = board[3][0:3] + board[4][0:3] + board[5][0:3]
        box5 = board[3][3:6] + board[4][3:6] + board[5][3:6]
        box6 = board[3][6:9] + board[4][6:9] + board[5][6:9]
        
        box7 = board[6][0:3] + board[7][0:3] + board[8][0:3]
        box8 = board[6][3:6] + board[7][3:6] + board[8][3:6]
        box9 = board[6][6:9] + board[7][6:9] + board[8][6:9]
        
        self.check(box1)
        self.check(box2)
        self.check(box3)
        self.check(box4)
        self.check(box5)
        self.check(box6)
        self.check(box7)
        self.check(box8)
        self.check(box9)
        
        return self.c
                    
        
        
