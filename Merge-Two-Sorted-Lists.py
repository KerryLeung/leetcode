# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
            
        if not l2:
            return l1
        
        head = l1 if l1.val < l2.val else l2
        current_pos = head
        
        while l1:
            if head == l1:
                l1 = l1.next
                continue
            
            if head == l2:
                l2 = l2.next
                continue
            
            if not l2:
                current_pos.next = l1
                l1 = l1.next
                current_pos=current_pos.next
                continue
            
            if l1.val < l2.val:
                current_pos.next = l1
                l1 = l1.next
                current_pos=current_pos.next
            else:
                current_pos.next = l2
                l2 = l2.next
                current_pos=current_pos.next
            
        while l2:
            current_pos.next = l2
            current_pos=current_pos.next
            l2 = l2.next
        
        return head
                
