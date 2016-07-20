# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
            
        if ( root.left and not root.right ) or (not root.left and root.right):
            return False
        
        def is_Symmetric(left, right):
            if (not left and right) or (left and not right):
                return False
            
            if not left and not right:
                return True
            
            if left.val != right.val:
                return False
            else:
                if left.left:
                    if not right.right or (left.left.val != right.right.val):
                        return False
                
                if left.right:
                    if not right.left or (left.right.val != right.left.val):
                        return False
                
                return is_Symmetric(left.left, right.right) and is_Symmetric(left.right, right.left)
                        
        return is_Symmetric(root.left, root.right)       
        
        
        
