'''


Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


'''

'''

I can't quite recall how this ones done

I think it's all about pointer management and using an effective function which is swapping the pointers.
I have gone wrong on the pointer management vs what the function returns.

Let's brainstorm what each does.

swapNodes - function, takes a pre node, and a post node. 

Can we swap the node and retrieve the next node?


Something like this...
(node.next,nextNode) = swapNodes(node,node.next)
node = nextNode

takes a tuple, returns a tuple. 

NOT THE CLEANEST EEK


'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode=ListNode(next=None)

        def swapNodes






'''

I think my rudimentery solution will involve a lot of pointers...

You need a main function to track where you begin and end a 'swap-list'.
Dummy at the start, count up until you reach the integer, keep the last pointer at the end
then re-arrange the nodes in the swap-set. 

[1,2,3,4,5,6,7,8]
[0,[1,2,3],4,5,6,7,8]
[0,[3,2,1],4,5,6,7,8]

[1,2,3]

pop off 3, store 4
3 [2,1]



'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def generateSwapSet(preNode,currentNode,l) -> tuple[ListNode,ListNode]:
            
            queue = deque([])


            while l>0:
                queue.append(currentNode)
                if currentNode.next is None and l != 1:
                    return False
                currentNode = currentNode.next            

            finalNode=currentNode
            while len(queue)>0:
                preNode.next=queue.pop()
                preNode=preNode.next
            preNode.next=finalNode
            return (preNode,finalNode)


        dummy = ListNode(next=head)
        swapTuple=generateSwapSet(dummy,head,k)
        while swapTuple:
            swapTuple = generateSwapSet(swapTuple[0],swapTuple[1],k)

        return dummy.next









