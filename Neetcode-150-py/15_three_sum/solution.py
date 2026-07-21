class Solution:
    # Time: O(?)
    # Space: O(?)
    def three_sum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res =[]
        n=len(nums)
        s = set()
        for i in range(n-2):
            ni=nums[i]
            j = i+1
            k=n-1
            while j!=k:
                nj=nums[j]
                nk=nums[k]
                total = ni+nk+nj
                if total ==0:
                    if not (ni,nj,nk) in s:
                        res.append([ni,nj,nk])
                        s.add((ni,nj,nk))
                    j+=1
                elif total <0:
                    j+=1
                elif total >0:
                    k-=1
        return res
