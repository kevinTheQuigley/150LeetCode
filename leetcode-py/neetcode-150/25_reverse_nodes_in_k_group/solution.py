'''

25. Reverse Nodes in k-Group

This is a 


'''


from leetcode_py import ListNode



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

