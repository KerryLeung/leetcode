# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        n1, n2 = l1, l2
        
        add_val = 0
        pNode = ListNode(0)
        head = pNode
        while n1:
            new_node = n1
            if n2:
                new_node.val += n2.val + add_val
                if new_node.val >= 10:
                    add_val = 1
                    new_node.val -= 10
                else:
                    add_val = 0
                n2 = n2.next
            else:
                if add_val == 1:
                    new_node.val += 1
                    if new_node.val >= 10:
                        new_node.val -= 10
                        add_val = 1
                    else:
                        add_val = 0
                
            n1 = n1.next
            pNode.next = new_node
            pNode = pNode.next
        
        while n2:
            new_node = n2
            if add_val == 1:
                new_node.val += 1
                if new_node.val >= 10:
                    new_node.val -= 10
                    add_val = 1
                else:
                    add_val = 0
            n2 = n2.next
            pNode.next = new_node
            pNode = pNode.next
  
        if add_val:
            pNode.next = ListNode(1)
            
        return head.next   
