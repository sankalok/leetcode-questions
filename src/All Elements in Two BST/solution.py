class Solution(object):
    def __init__(self):
        self.result = []
        
    def inorder(self, root):
        if(root != None):
            self.inorder(root.left)
            self.result.append(root.val)
            self.inorder(root.right)
    
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        inorder(root1, result)
        """
        
        self.inorder(root1)
        self.inorder(root2)
        
        return(sorted(self.result))
