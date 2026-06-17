'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


'''

'''
pop one off recursively call an algorithm, then return the final result



'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letDict={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def generateLetters(inputStr,remainingDigits):
            if remainingDigits =="":
                return [inputStr]
            else:
                returnList = []
                letters = letDict[remainingDigits[0]]
                for letter in letters:
                    returnList.extend(generateLetters(inputStr+letter,remainingDigits[1:]))
                return returnList
            
        return generateLetters('',digits)






'''
This reminds me of factorial questions, choosing random combinations.

My instinct is telling me the brute force solution is probably correct.

Need to track the new digits with a list of lists.  

Some string functions like 'extend' might come in handy

s1 = ['a','b','c']
s1=''

s2 = 'def'

for char in s1:
    for substring in s2:
        print(char+substring)
newString = [substring+char for substring in s1 for char in s2]
print(s1)
        
        
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letDict={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        charList=None

        while len(digits)>0:

            d=digits[0]
            digits=digits[1:]

            if charList is None:
                nextCharList=[char for char in letDict[d]]
            else:
                nextCharList=[]
                for char in charList:
                    for substring in letDict[d]:
                        nextCharList.append(char+substring)
            charList=nextCharList
        if charList is None:
            return []
        else:
            return charList
