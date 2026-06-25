'''


'''

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        # Three pointers get tricky, isolat the first pointer (i) at the start
        # Move the second (j) and third (k) pointers towards eachother depending on their positions
        # Iterate over time
        # Append all three pointers if they reach 0
        # If i>0, end the iteration
        n1 = len(nums)
        i = 0

        res = []

        s = set()
        while nums[i]<=0 and i < (n1-2):
            j = i+1
            k = n1-1


            while j!=k:

                val = nums[i]+nums[j]+nums[k]
                if val==0:
                    if (nums[i],nums[j],nums[k]) not in s:
                    
                        res.append([nums[i],nums[j],nums[k]])
                        s.add((nums[i],nums[j],nums[k]))
                    k-=1
                
                if val >0:
                    k-=1
                elif val<0:
                    j+=1

            i+=1
        return res
