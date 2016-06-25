# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        s=head
        m=s.next
        
        while m != None:
            if m.val == s.val:
                while m.val == s.val:
                    if m.next != None:
                        m=m.next
                    else:
                        s.next=None
                        return head
                s.next=m
            else:
                s=s.next
                m=m.next
        return head
            
            
            
