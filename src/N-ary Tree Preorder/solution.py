class Solution(object):
    def __init__(self):
        self.p = []
        
    def p_order(self, root):
        if(root != None):
            self.p.append(root.val)
            for child in root.children:
                self.p_order(child)
        
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.p_order(root)
        
        return self.p
