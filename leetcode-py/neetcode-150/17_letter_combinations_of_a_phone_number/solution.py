class Solution:
    # Time: O(?)
    # Space: O(?)
    def letter_combinations(self, digits: str) -> list[str]:
        # Recursive function that repeatedly recalls and splits the digits

        if not digits:
            return []

        d_dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def addVals(remaining_digits,path):
            if remaining_digits=="":
                res.append(path)

                return
            
            digit = remaining_digits[0]

            letters = d_dict[digit]

            for letter in letters:
                addVals(remaining_digits[1:],path+letter)

        addVals(digits,"")

        return res