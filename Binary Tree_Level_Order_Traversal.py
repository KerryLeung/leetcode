# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res={}
        
        def find_path(root, level):
            if root.left == None and root.right == None:
                pass
            if root.left != None:
                if not res.has_key(level):
                    res[level]=[]
                res[level].append(root.left.val)
                find_path(root.left, level+1)
            if root.right != None:
                if not res.has_key(level):
                    res[level]=[]
                res[level].append(root.right.val)
                find_path(root.right, level+1)
                
        res[0]=[root.val]
        find_path(root, 1)

        return [ v for v in res.values()]
            
        
