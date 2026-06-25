


'''
How to visualise the split






'''


from math import inf
class Solution:
    # Time: O(?)
    # Space: O(?)
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        # TODO: Implement find_median_sorted_arrays

        n1=len(nums1)
        n2 = len(nums2)

        if n1>n2:
            return self.find_median_sorted_arrays(n2,n1)
        

        par = (n1+n2)/2
        b1 = 0
        b2 = n1

        while b2!=b1:
            l1 = b1+b2/2
            r1 = b1+b2/2 +1

            l2 = par-l1+2
            r2 = l2+1

            l1v = nums1[l1] if l1>=0 else -inf
            r1v = nums1[r1] if r1<n1 else inf
            l2v = nums2[l2] if l2>=0 else -inf
            r2v = nums2[r2] if r2<n2 else inf

            if r1v <l2v:
                b1 = l1+1
            elif r1v>l2v:
                b2 = r1-1
            else:
                if par %2:
                    return (max(l1v,l2v) +min(r1v,r2v))/2
                else:
                    return max(l1v,l2v)




        

