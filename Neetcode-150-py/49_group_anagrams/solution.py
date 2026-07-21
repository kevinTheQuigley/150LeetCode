class Solution:
    # Time: O(?)
    # Space: O(?)
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        def find_ord(s):
            ord_list = [0]*26

            for char in s:
                n = ord(char)-ord("a")
                ord_list[n]+=1


            return tuple(ord_list)
        ord_dict = {}

        for st in strs:
            ord_st = find_ord(st)
            if ord_st in ord_dict:
                ord_dict[ord_st].append(st)
            else:
                ord_dict[ord_st]=[st]
        return_res = []
        for ord_st in ord_dict:
            return_res.append(ord_dict[ord_st])


        return return_res
