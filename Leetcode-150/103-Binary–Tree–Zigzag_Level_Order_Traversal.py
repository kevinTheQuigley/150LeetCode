# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Have some iterator that keeps track of the level
odd -> left to right
even -> right to left
nextList -> Keeps track of next set of elements
currentList -> Elements are popped out of this list

May not need a deque
Is there a smart way of doing this? If working left to right,
append left child, then right child, work to next node.

Then were working right to left, append right child then left child
Still need a 'nextList' and a currentList, but we can use a stack instead.
(or a list, just using pop)
'''
from collections import deque 


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level=1
        currentLevel = [root]
        returnList = [[root.val]]

        while len(currentLevel)>0:
            nextLevel = deque([])
            appendList = []

            if level %2:
                while len(currentLevel)>0:
                    node = currentLevel.pop()
                    if node.right:
                        appendList.append(node.right.val)
                        nextLevel.append(node.right)
                    if node.left:
                        appendList.append(node.left.val)
                        nextLevel.append(node.left)
            
            else:
                while len(currentLevel)>0:
                    node = currentLevel.pop()
                    if node.left:
                        appendList.append(node.left.val)
                        nextLevel.append(node.left)
                    if node.right:
                        appendList.append(node.right.val)
                        nextLevel.append(node.right)
            if appendList:
                returnList.append(appendList)
            currentLevel = nextLevel
            level+=1

        return returnList

