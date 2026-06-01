# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''

I think the fastest solutions are O~ log(n)

Quick sort? - Split sort? 

involves splitting the LIST into smaller and smaller subdivisions. 
Compare each subdivision one unit at a time.

Start with the original node, get halfway, use a recursive function to get a pointer to every node.

Bubble sort?
Find the smallest element. Bring pop it out, bring it to the start. repeat recursively
n^2

Function to find the smallest. 
Needs
1. The previous node to the smallest node (For the pointer)
2. The smallest node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Merge sort
# Function which will split the list of nodes in two, returns mid node
# Function which merges two lists of the same length, returns first node

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        def splitNodeList(headNode):
            slow,fast = headNode,headNode

            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            
            midNode = slow.next
            slow.next=None
            
            return midNode
        
        def joinNodeList(headNode_1,headNode_2):
            dummyNode=ListNode()
            currentNode = dummyNode

            while headNode_1 and headNode_2:
                if headNode_1.val > headNode_2.val:
                    currentNode.next = headNode_2
                    headNode_2 = headNode_2.next
                else:
                    currentNode.next = headNode_1
                    headNode_1 = headNode_1.next
                currentNode=currentNode.next
            
            if headNode_1:
                currentNode.next = headNode_1
            elif headNode_2:
                currentNode.next = headNode_2

            
            return dummyNode.next

        def mergeSort(node):
            if node and node.next:
                midNode = splitNodeList(node)
                node = mergeSort(node)
                midNode = mergeSort(midNode)
                node = joinNodeList(node,midNode)
                return node
            else:
                return node

        
        return mergeSort(head)


            

            

