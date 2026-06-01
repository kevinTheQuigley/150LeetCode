# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Working down from the root, 
the second level has to be less then the root if on left, 
greater then the root if on the right.

Get's more confusing for the following layers


        5
       / \
    3       6
   /      /    \
  1      4      7

  
Looking at the nodes above the node range is narrowed between two values, the parents govern the range
need a function that takes both parents (One of which could be None)

returnValue = True

    




        




def checkNode(node,leftParent,rightParent):
    lowerNodes = checkNode(node.left,leftParent,node) and checkNode(node.right,node,rightParent)
    if not node:
        return True
    if leftParent and rightParent:
        return (leftParent.val<node.val) and (node.val<rightParent.val) and lowerNodes
    elif leftParent:
        return (leftParent.val<node.val) and lowerNodes
    elif rightParent:
        return (node.val<rightParent.val) and lowerNodes

if not root:
     return True

checkNode(root,None,None)


recursive call 1
5,None,None  -> calls checkNode(4,5,None)


recursive call 2
4,5,None
5<4 
0 & 1 -> 0



'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        