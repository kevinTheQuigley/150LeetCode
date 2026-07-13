'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


'''

'''


'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2 = len(nums2)

        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        
        par = n1+n2/2

        bl1 = 0
        br1 = n1-1

        while bl1 <br1:
            
            l1 = (bl1+br1)//2

            r1 = (l1+1)
            

            l2 = par-l1
            r2 = (l1+1)
            
            if l1 <0:
                l1Val = -inf
            elif r1 > n1-1:
                r1Val = inf
            if l2 <0:
                l2Val = -inf
            if r2 >n2-1:
                r2Val = inf
            
            if l1Val > r2Val:
                br1 = l1-1
            elif l2Val >r1Val:
                bl1 = l1+1

        if par%2==0:
            return (max(l1Val,l2Val)+min(r1Val,r2Val))/2
        else:
            return (max (l1Val,l2Val))
                
























class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1= len(nums1)
        n2= len(nums2)

        if n2>n1:
            return self.findMedianSortedArrays(n2,n1)

        part = (n1+n2)//2

        bl1=0
        br1=n1-1

        while bl1 < br1:
            l1 = (bl1+br1)//2
            r1 = l1+1


            l2 = part-l1
            r2 = l2+1

            if nums1[l1] > nums2[r2]:
                br1=l1-1
            elif nums1[r1] < nums2[l2]:
                bl1=r1+1
            else:
                return (max(nums1[l1],nums2[l2])+min(nums1[r1],nums2[r2]))



























from math import inf



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)
        # start with the largest one as nums1

        if n2>n1:
            return self.findMedianSortedArrays(nums2,nums1)
        
        part=(n1+n2)/2

        bl1=0
        br1=n1-1

        bl2=0
        br2=br1-part

        l1= int((br1-bl1)/2)
        r1=l1+1

        l2 = int((bl2+br2)/2)
        r2 = l2+1

        while nums1[l1]>nums2[r2] or nums1[r1]< nums2[r2]:

            if nums1[l1] >nums2[r2]:
                br1=l1-1
            else:
                bl1=l1+1



























class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)
        if n2>n1:
            return self.findMedianSortedArrays(nums2,nums1)

        bdl = 0
        bdr = n1
        n = n1+n2

        part = (n1+n2+1)/2

        while bdl<bdr:

            l1=l2=-inf
            r1=r2=inf

            mid = (bdl+bdr)/2

            if mid <n1:
                r1 = nums1[mid]
            if (part-mid)<n2:
                r2 = nums2[part-mid]
            if mid > 0:
                l1 = nums1[mid-1]
            if  (part-mid)> 0:
                l2 = nums2[part-mid-1]
            
            if (l1 <r2) and (l2<r1):
                if n%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return (max(l1,l2))
                
            if l1>r2:
                bdl=mid+1
            else:
                bdr=mid-1



        
        return 0



















'''

--------  ---

------ ------
--

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)<len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        len1 = len(nums1)
        len2 = len(nums2)

        total_len=len1+len2

        bdl1=0
        bdr1=total_len

        bdl2=0
        bdr2=total_len/2 - len2
        l1 = (bdl1+bdr1)/2
        r1 = l1+1

        l2= (bdl2+bdr2)/2
        r2 = l2+1

        



        while nums1[l1]>nums2[r2] or nums2[l2]>nums1[r1]:
            if nums1[l1] > nums2[r2]:
                l1 = 



























'''
How do we kick things off? 
Split the two arrays in (roughly) half, begin by always having the larger array first and the smaller array second

total length = (len1+len2)/2-> halway

pos2 = len1


# Do we use the 'bounds' to figure what possible updates we make? -> Yes in this solution we do use bounds -> A low and a high
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) <len(nums2):
            (nums1,nums2)=(nums2,nums1)
        
        len1=len(nums1)
        len2=len(nums2)

        pos1=(len1+len2)/2
        pos2=len1-(len1+len2)/2

        l1=nums1[pos1]
        r1=nums1[pos1+1]
        l2=nums2[pos2]
        r2=nums2[pos2+1]

        while l1>r2 or l2>r1:
            if l1>r2:
                # Update the values of l1 downwards -> 
                # Amount of update 



        

            
        
        






















'''
There must be an equal number of numbers on one side as there is on the other. 

We use two pointers to keep track within both arrays, as they are both ordered. [l1,r1,l2,r2]

constraints:-
l1=r1-1
l2=r2-1
l1<r2
l2<r1

# Target 
l1+l2=(len1+len2+1)/2

when target met, chose the biggest l and smallest r

while  l1<



Here we go again! Lets try get these expressions together:-

total number of values = len(nums1)+len(nums2) (call them size_1 and size_2)

use these values to track your position in the cell l1,r1,l2,r2 -> 

Make adjustments based on this formula for binary search 
begin with

l1=(0+size_1)/2

l2=(size_1+size_2) -l1 

What can kind of confuse me sometimes is not having the boundary values.
Normally I associate binary search with pushing left and right pointers gradually towards eachother in a list
This time we balance one first, and then the other.

What is this update equation? Adjustment size needs to get smaller over time - Like a usual binary search. 
How can we mediate this? we keep our rules about partition size true at all times 

if l1>l2:




We work towards a situation where 
l1<l2<r1<r2





'''
























'''

Leetcode Hard lol

log(m+n) -> indicates it's a binary search problem
Do we just join the two arrays together? How can we binary search two things at once?

What if array 1 [1,2,3,4,5]
and array 2 is like [6,7,8,9]?

Begin by checking the middle value of both. 
There then should be an equation to find the balance of the two.
average 
(m+n)/2 numbers

check first and last values of the two arrays. 
instead of jumping down m/2, compare them and take some kind of relative gap?
probably these jumps should be relative to the sizes of the arrays,

m/2,n/2
m/4,n/4 etc
balance the number on the left to the number on the right, ie the sum of values to either side should be m+n/2.
Track the total on either side, and keep pushing them up or down, by relative amounts


we have two pointers for each list, and we aim to have the pointers such that 

l1 <=l2 <=r1<=r2

take the example 
nums1 = [1, 3, 8] ->len_l1=3
nums2 = [7, 9, 10, 11] ->len_l2=4

l1=(0+len_1)/2 =1.5
r1=l1+1 =2

l2=(len_1+len_2+1)/2-l1
r2=l2+1



'''





















class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)


        



















class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        target = int((m+n)/2)

        left1 = left2 = 0
        right1 = m-1
        right2 = n-1

        while (left1+left2)!=target:
            index1=(left1+right1)/2
            index2=(left2+right2)/2

            val1=nums1[index1]
            val2=nums2[index2]
            if val1>val2:
                ...



