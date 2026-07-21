'''
class Solution:
    # Time: O(?)
    # Space: O(?)
    def plus_one(self, n:list) -> list:
        return list





'''
class Solution:
    # Time: O(?)
    # Space: O(?)
    def plus_one(self, nums:list) -> list:

        extra=1
        n = len(nums)

        for i in range(n):
            num = nums[-i-1]
            num+=extra
            if num//10:
                nums[-i-1]=0
            else:
                break


        return nums


