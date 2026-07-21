class Solution:
    # Time: O(?)
    # Space: O(?)
    def letter_combinations(self, digits: str) -> list[str]:
        letDict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if digits=="":
            return []   
        res = []
        n=len(digits)
        
        def process_digit(digit_num,path):
            if digit_num==n:
                res.append(path)
            else:
                digit = digits[digit_num]
                letters = letDict[digit]



                for letter in letters:
                    process_digit(digit_num+1,path+letter)
                
        process_digit(0,"")
        # TODO: Implement letter_combinations
        return res
