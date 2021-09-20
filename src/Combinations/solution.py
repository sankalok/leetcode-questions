from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(1, n+1):
            arr.append(i)
        result = []
        for c in combinations(arr, k):
            result.append(list(c))
        return result
        
