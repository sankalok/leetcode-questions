import math
class Solution(object):
    def __init__(self):
        self.bstL = []
        
    def inorder(self, root):
        if(root != None):
            self.inorder(root.left)
            self.bstL.append(root.val)
            self.inorder(root.right)
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        self.bstL.sort()
        
        if(len(self.bstL) == 2):
            return abs(self.bstL[0] - self.bstL[1])
        
        mininum = 0
        minimum = abs(self.bstL[0] - self.bstL[1])
        for i in range(1, len(self.bstL)):
            if(abs(self.bstL[i] - self.bstL[i-1]) < minimum):
                minimum = self.bstL[i] - self.bstL[i-1]
        return minimum
        
