import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = m-1+n-1
        R = m-1
        return factorial(N)/(factorial(R)*factorial(N-R))
