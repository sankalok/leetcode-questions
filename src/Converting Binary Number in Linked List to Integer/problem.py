# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binaryString = ""
        node = head
        while(node != None):
            binaryString += str(node.val)
            node = node.next
        length = len(binaryString)
        decimalValue = 0
        while(head != None):
            decimalValue += ((2 ** (length - 1)) * head.val)
            length -= 1
            head = head.next
        return decimalValue
