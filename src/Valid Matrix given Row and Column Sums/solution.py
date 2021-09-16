import math
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        result = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        
        for i in range(0, len(rowSum)):
            for j in range(0, len(colSum)):
                result[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= result[i][j]
                colSum[j] -= result[i][j]
        
        return result
