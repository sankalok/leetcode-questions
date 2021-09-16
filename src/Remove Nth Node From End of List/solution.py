class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        temp = head
        lenList = 0
        while(temp != None):
            lenList += 1
            temp = temp.next
            
        temp = head
        
        if(lenList == 1):
            head = None
            return head
        
        if(n == 1):
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
            return head                
        
        position = lenList - n
        for i in range(0, position):
            temp = temp.next
    
        temp.val = temp.next.val
        temp.next = temp.next.next
           
        
        return head
