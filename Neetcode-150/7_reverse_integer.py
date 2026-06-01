'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Just use a mod, shrink the number, compute the max and check if it is about to achieve the max before continuing 

class Solution:
    def reverse(self, x: int) -> int:

'''

'''

Just need to keep track of the boundaries. Wait for the number to get close, then check if it's getting too large

'''


class Solution:
    def reverse(self, x: int) -> int:

        rev=0
        upper=(2**31)-1
        lower=2**31

        if x<0:
            bound = lower
            isNeg=True
        else:
            isNeg=False
            bound=upper
        
        
        while 0<x<bound:
            rev*=10
            rev+=x%10
            x//=10

        if x>bound:
            return 0
        
        if isNeg:
            return -rev
        else:
            return rev

















class Solution:
    def reverse(self, x: int) -> int:
        maxPos = 2**31-1
        maxNeg = -2**31
        isNeg=1
        if x <0:
            isNeg=-1

        x*=isNeg
        
        returnNum=0
        i=0

        while x>0 and returnNum<maxPos//10 and returnNum>maxNeg//10:
            remainder = x%10
            returnNum*=10
            returnNum+=remainder
            x //=10
        returnNum*=isNeg
        return returnNum

        
        



'''




'''























'''

Naively, I think we should use combination of mod and another to keep track of the remainder, 
and keep adding it back.
I wonder if there's some way we could use dynamic programming?

We should insert a check at the point where the integer would be ABOUT to get bigger then a 32 bit signed integer,
if the integer fails the check then we proceed. 

'''


class Solution:
    def reverse(self, x: int) -> int:
        returnNum = 0 

        while x :
            returnNum*=10
            latest = x%10
            x=x//10
            if x<0:
                negative=True
                x*=-1

            returnNum+=latest



            if (returnNum <-2**32%10 or returnNum>=(2**32-1)%10) and x>4:
                return 0
        return returnNum
            

