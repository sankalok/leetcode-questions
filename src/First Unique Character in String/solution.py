class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in s:
            c = s.count(i)
            if(c == 1):
                return s.index(i)
        return -1 
        
