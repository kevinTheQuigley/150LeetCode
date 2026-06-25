'''

25. Reverse Nodes in k-Group

This is a 


focus on splitting the function into pieces 


a       b       c...
current next    ...

'''

# A lot of variables here
from leetcode_py import ListNode




class Solution:
    # Time: O(?)
    # Space: O(?)
    def reverse_k_group(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:
        dummy = ListNode(next = head,val=None)
        firstDummy = dummy

        currentNode = head

        i = k

        stack = []
        while currentNode is not None:

            stack.append(currentNode)
            nextNode = currentNode.next
            if i==1:

                while len(stack)>0:

                    dummy.next = stack.pop()
                    dummy=dummy.next

                dummy.next = nextNode

                i=k
            else:

                i-=1
            currentNode = nextNode
        return firstDummy.next



            









'''
class Solution:
    # Time: O(?)
    # Space: O(?)
    def reverse_k_group(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:

        dummy = ListNode(val=None,next=head)
        zero_k = dummy

        i = 0

        stack = []
        while head.next is not None:
            stack.append(head.next)
            head = head.next
            i+=1
            if i ==k:
                next_k=head.next
                zero_k.next = stack[-1]
                # unpack the stack...

                while len(stack)>0:
                    zero_k.next = stack.pop()
                    zero_k=zero_k.next
                zero_k.next=next_k
                i=0
                head = zero_k

                stack = []
        return dummy.next

'''