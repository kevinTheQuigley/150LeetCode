'''


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
'''

'''
naively imagining you could do an initial sort of all K listNodes, to put them in order.
Would you recreate each pointer with an empty pointer? -> create a new series of pointers?
Lose awareness of what the old pointer pointed at.

[
  1->4->5,
  1->3->4,
  2->6
]

suppose you do an initial sort, and 
place each pointer into a kind of stack where you sort the dummy pointer after popping out the one your interested in.

listNodes:-[
  1->4->5,
  1->3->4,
  2->6
]

listNodes.pop(dummy)

dummy       -> 4->5
returnDummy -> 1
returnList  -> 1

listNodes:-[
  1->3->4,
  2->6
] -> insert dummy 4->5 then sort

yields:-
listNodes:-[
  1->3->4,
  2->6
  4->5
]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        #tupleList=[(node.val,node) for node in lists]
        tupleList =[]
        i=0
        for node in lists:
            if node:
                tupleList.append((node.val,i,node))
            i+=1

        
        tupleList.sort(reverse=True)

        dummyReturn = ListNode()
        dummyNode = dummyReturn

        while len(tupleList)>0:
            dummyNode.next=tupleList.pop()[2]
            dummyNode=dummyNode.next
            if dummyNode.next:
                tupleList.append((dummyNode.next.val,i,dummyNode.next))
            tupleList.sort(reverse=True)
            i+=1
        return dummyReturn.next



