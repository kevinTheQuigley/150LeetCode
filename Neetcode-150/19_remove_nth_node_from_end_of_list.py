'''

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       

'''

'''

Classic two pointer solution to a linked list. Iterate two pointers. 
Wait for one of them to get to be counting out towards the end of the list,
before initialising the second pointer. 



'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        firstPointer=head
        dummy = ListNode(next=head)

        while n>0:
            firstPointer=firstPointer.next
            n-=1
        secondPointer=dummy
        if firstPointer is None:
            print('fp is none')
        while firstPointer is not None:
            firstPointer=firstPointer.next
            secondPointer=secondPointer.next
            
        if secondPointer is head:
            return head.next 
        else:
            secondPointer.next = secondPointer.next.next
            return head
        
