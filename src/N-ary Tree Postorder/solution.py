class Solution(object):
    def __init__(self):
        self.p = []
        
    def p_order(self, root):
        if(root != None):
            for child in root.children:
                self.p_order(child)
            self.p.append(root.val)
        
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.p_order(root)
        
        return self.p
