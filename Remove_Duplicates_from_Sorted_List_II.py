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

        i=s=head
        m=s.next   
        if s.val == m.val and m.next== None:
            return None
            
        while m != None :
            if m.val == s.val:
                if m.val == head.val:
                    while m.val == head.val:
                        if m.next != None:
                            m=m.next
                        else:
                            return None
                    head=m
                    s=head
                    m=s.next
                else:
                    while m != None and m.val == s.val :
                        m=m.next
                    i=head
                    while i.next != s:
                        i=i.next
                    i.next=m
                    if m == None:
                        return head
                    s=m
                    m=s.next
            else:
                s=s.next
                m=s.next
        return head
        
