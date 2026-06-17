'''
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length



When picking pairs, you can go either one up, or one down, in either direction:-

[a,1]

[b,1]

[a,2]

Deciding on a pair depends on the difference in values, and if the previous pair has been selected or not. 
Would it be worth storing the old pairs in some kind of visited dictionary?
One issue is that numbers can have the same value, so the dictionary would need to be based on position, not value.

If a pair has the same value, it should be the next to be chosen

list1 = [1,4,5,7,9]
list2 = [1,7,7,7,9]

track points in list with two pointers, [i,j]
if l1[i+1]+l[j] < l1[i]+l[j+1] -> Iterate over j -> repeat. If equal just iterate over j


Naive solution is caught out when you can iterate downwards and add upwards on either side


[1,2,4,5,6]
[3,5,7,9]

[1,3],[2,3],[1,5],[2,5]

This fails when there was a lower combination that wasn't investigated. 

Suppose you stored the values which hadn't been visited in a dictionary, and then removed them as they get used.

start with 
[1,3]

then add both of these values. Your either iterating on the top or on the bottom

every time you have the two options your choosing between 

more like 

[1,3]

[2,3] OR  [1,5]



[4,3],[2,5] OR [2,3]


How do you know which side to iterate over?
Save as left tuples and right tuples?



4,5,6,7


What is a heap?

I imagine a list, but it's probably more like a binary tree. Every element from left to right is smaller then the next

'''




class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        returnList = []
        i,j=0,0
        if k==0:
            return returnList
        returnList.append([nums1[0],nums2[0]])

        leftTuples=[[nums1[1],nums2[0]]]
        rightTuples=[[nums1[0],nums2[1]]]

        while len(returnList)<k:

            leftTuples_next = leftTuples
            if (nums1[i+1]+nums2[j]) <=(nums1[i]+nums2[j+1]):
                i=i+1
            else:
                j=j+1
            returnList.append([nums1[i],nums2[j]])
        return returnList
            

        

'''

Two arrays, find the smallest possible combination.

This is a 'Heap' problem

We start with the most basic solution (0,0) for both lists, then add the values to the heap, tracking them throughout, 
and popping the top value to track where we are

A dict won't do to track the values. Need to track them within the heap

How to create a heap? - A heap is a Binary tree structure where every sub elemeent has two smaller elements

def node(value):



'''