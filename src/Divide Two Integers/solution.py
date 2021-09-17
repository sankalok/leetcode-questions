class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = float(dividend)/float(divisor)
        if(result != float(dividend//divisor)):
            if(result < 0):
                if(result <= -2**31):
                    return -2**31
                return int(result)
        if(result >= 2**31 - 1):
            return (2**31 - 1)
        return (dividend//divisor)
            
