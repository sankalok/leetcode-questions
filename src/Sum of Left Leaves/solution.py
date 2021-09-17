class Solution(object):
    def __init__(self):
        self.sum = 0
        
    def inorder(self, root):
        if(root != None):
            self.inorder(root.left)
            if(root.left != None and root.left.left == None and root.left.right == None):
                self.sum += root.left.val
            self.inorder(root.right)
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        return self.sum
        
