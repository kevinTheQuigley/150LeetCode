'''
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

I think it would make sense to use a heap:-> 
push back the node by its value into the heap.



heapq.heapify(list)

'''

from leetcode_py import ListNode
from heapq import heapppush


class Solution:
    # Time: O(?)
    # Space: O(?)
    def merge_k_lists(self, lists: list[ListNode[int] | None]) -> ListNode[int] | None:
        lists.sort(key=lambda x:x.val)


        returnDummy = ListNode(val=None,next = lists[0])
        current = returnDummy.next

        while lists:

            current.next = lists.pop(0)
            current = current.next
            next = current.next 

            if next:
                lists.heappush()


        # TODO: Implement merge_k_lists
        return returnDummy.next
