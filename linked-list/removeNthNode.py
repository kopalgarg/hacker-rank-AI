# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        Pointer = head
        nthPointer = head
        
        for _ in range(n):
            Pointer = Pointer.next
            
        if not Pointer:
            return head.next
    
        while Pointer.next:
            Pointer = Pointer.next
            nthPointer = nthPointer.next
        
        nthPointer.next = nthPointer.next.next
        
        return head
            
            
            
                
                