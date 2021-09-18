class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = [None]*maxSize
        self.top = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if(self.top != len(self.stack)):
            self.stack[self.top] = x
            self.top += 1
        

    def pop(self):
        """
        :rtype: int
        """
        if(self.top == 0):
            return -1
        else:
            self.top -= 1
            return self.stack[self.top]
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if(k <= self.top):
            for i in range(0, k):
                self.stack[i] += val
        else:
            for i in range(0, self.top):
                self.stack[i] += val
        
