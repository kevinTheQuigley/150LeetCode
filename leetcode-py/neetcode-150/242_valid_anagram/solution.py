class Solution:
    # Time: O(?)
    # Space: O(?)
    def is_anagram(self, s: str, t: str) -> bool:
        main_dict= {}

        for i in s:
            if i in main_dict:
                main_dict[i]+=1
            else:
                main_dict[i]=1
        
        for j in t:
            if not j in main_dict:
                return False
            main_dict[j]-=1
            if main_dict[j]==0:
                main_dict.remove(j)
        if len(main_dict)>0:
            return False
        else:
            return True
