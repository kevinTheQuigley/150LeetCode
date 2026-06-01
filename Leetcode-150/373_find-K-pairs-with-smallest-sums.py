'''
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
            

        

