'''You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


 Definition for singly-linked list.


Iterate over both lists at once, adding the numbers at the 1st,2nd,3rd positions, recording any remainder. 
We could work from the shortest list, or add an if else statment to check if were out of range. Probably easiest to use the shortest range.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        remainder = 0
        dummyNode = ListNode()
        startNode = ListNode(next=dummyNode)

        while l1 or l2 or remainder:
            dummyNode.next = ListNode()
            dummyNode= dummyNode.next
            total = 0 
            if l1:
                total+=l1.val
                l1=l1.next

            if l2:
                total+=l2.val
                l2=l2.next

            total+=remainder

            remainder = total//10
            total = total%10

            dummyNode.val=total
        
        return startNode.next.next




        



















class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1=ListNode(val=0,next=l1)
        dummy2=ListNode(val=0,next=l2)
        dummyReturn=ListNode(val=0,next=None)
        firstDummy = ListNode(val=0,next=dummyReturn)
        remainder=0

        while l1 or l2 or remainder:
            nextVal=0

            if l1:
                nextVal+=l1.val
                l1=l1.next
            if l2:
                nextVal+=l2.val
                l2=l2.next
            if remainder:
                nextVal+=remainder
            
            dummyReturn.val = nextVal%10
            dummyReturn.next=ListNode()
            dummyReturn=dummyReturn.next

            
            remainder = nextVal//10




        return firstDummy.next

        
                    