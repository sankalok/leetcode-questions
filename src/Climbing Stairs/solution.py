from collections import defaultdict
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = defaultdict(list)
        
        result[1] = 1
        result[2] = 2
        
        if(n == 1 or n==2):
            return result[n]
        
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2]
            
        return result[n]
        
