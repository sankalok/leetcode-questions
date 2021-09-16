#User function Template for python3
import math
class Solution:
    def squaresInChessBoard(self, N):
         # code here
        totalSquares = 0
        for i in range(1, N+1):
            totalSquares += pow(i,2)
        return totalSquares
