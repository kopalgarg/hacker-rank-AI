class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        curA = headA
        curB = headB
        lenA = 0
        lenB = 0
        # compute lengths 
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        # reset to head 
        curA = headA
        curB = headB
        # bring to the same index by computing diff
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        else:
            for i in range(lenB-lenA):
                curB = curB.next
        # see where they start having the same val
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
            
            
        