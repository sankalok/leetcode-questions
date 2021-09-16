class Solution(object):
    def __init__(self):
        self.bstL = []
        
    def inorder(self, root):
        if(root != None):
            self.inorder(root.left)
            self.bstL.append(root.val)
            self.inorder(root.right)
            
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.bstL
