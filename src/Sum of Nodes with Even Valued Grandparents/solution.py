# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):  
    def __init__(self):
        self.s = 0
        
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root != None):
            if(root.val % 2 == 0):
                if(root.left != None):
                    if(root.left.left != None):
                        self.s += root.left.left.val
                    if(root.left.right != None):
                        self.s += root.left.right.val
                if(root.right != None):
                    if(root.right.left != None):
                        self.s += root.right.left.val
                    if(root.right.right != None):
                        self.s += root.right.right.val
            # print(self.s)
            self.sumEvenGrandparent(root.left)
            self.sumEvenGrandparent(root.right)
        return self.s
