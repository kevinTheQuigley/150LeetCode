'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
'''

'''
Pretty straightforward, two pointers, one at each list. 
Iterate over both and check values to see which one is bigger. 
Chose the smaller one as the next lead node

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        headNode = dummyNode

        while  not (list1 is None or list2 is None):

            if list1.val >list2.val:
                dummyNode.next = list2
                list2=list2.next
                dummyNode=dummyNode.next
            else:
                dummyNode.next=list1
                list1=list1.next
                dummyNode=dummyNode.next

        else:
            if list1 is None:
                dummyNode.next=list2
            else:
                dummyNode.next=list1
        return headNode
            



