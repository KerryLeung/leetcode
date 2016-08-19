# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if n < 0 or not head or (n == 1 and head.next == None):
            return

        i, length = 0, 0
        s = head
        while s:
            s = s.next
            length += 1
        s = head
        if n > length:
            n = n % length

        n = length -n
            
        while i < n-1:
            s = s.next
            i += 1
        
        if n == length-1:
            s.next = None
        elif n == 0:
            head = head.next
        else:
            e = s.next.next
            s.next = e
        return head
        
