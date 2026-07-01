



from math import inf
class Solution:
    # Time: O(?)
    # Space: O(?)
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1>n2:
            return self.find_median_sorted_arrays(nums2,nums1)

        hi = n1
        lo = 0
        mid = (n1+n2+1)//2

        while hi >=lo:
            lp1 = (hi+lo)//2
            lp2 = mid-lp1

            l1=nums1[lp1-1] if (lp1-1>=0) else -inf
            r1=nums1[lp1] if (lp1<n1) else inf
            l2=nums2[lp2-1] if (lp2-1>=0) else -inf
            r2=nums2[lp2] if (lp2<n2) else inf

            if l1 >r2:
                hi=lp1-1
            elif l2>r1:
                lo = lp1+1
            else:
                if (n1+n2)%2:
                    return max (l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2


