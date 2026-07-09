'''


use a set, 
check each word against a set of values, 
create an associated set if there is a list. 

One option that comes to mind is to sort the letters in the word. 
We could convert them to 'ord' ints.

I feel like their could be a cleaner way.

We have a set, and pop characters out of it. 
If it doesn't exist then we add it.

Do we have a set of sets? 
And pop each char out of every set every time?

N different words -> have to pop a char out N words l times where l is word length


Lets say we have a set of words

'''

class Solution:
    # Time: O(?)
    # Space: O(?)
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:

        c_dict = {}



        for word in strs:
            if word =="":
                c_dict[""]==""
            else:
                s = set(word)
                k = str(s)
                if k in c_dict:
                    c_dict[k].append(word)
                else:
                    c_dict[k] = [word]
        res = []
        for key in c_dict:
            res.append(c_dict[key])
            
        return res
    
