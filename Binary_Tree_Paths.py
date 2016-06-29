# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        res=[]
        def find_path(root, path):
            if root.left == None and root.right == None:
                res.append(path)
            if root.left != None:
                find_path(root.left, path+'->'+str(root.left.val))
            if root.right != None:
                find_path(root.right, path+'->'+str(root.right.val))
        
        find_path(root, str(root.val))
        return res
