# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return root        

        elif root in [p,q]:
            return root
        
        lca_l = lowestCommonAncestor(root.left,p,q)
        lca_r = lowestCommonAncestor(root.right,p,q)

        if lca_l and lca_r:
            return root
        elif lca_l:
            return lca_l
        elif lca_r:
            return lca_r

        


        

        
