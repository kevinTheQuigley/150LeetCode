'''
Here the trick is to iterate over, gradually reducing the target, and iteravely call the backtrack solution


'''



class Solution:
    # Time: O(?)
    # Space: O(?)
    def combination_sum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # TODO: Implement combination_sum2

        candidates.sort()

        res_list=[]

        def backtrack(remainder,i,path):
            if remainder ==0:
                res_list.append(path)

            j=i
            while j <len(candidates):

                if remainder- candidates[j]<0:
                    break
                backtrack(remainder-candidates[j],j+1,path+[candidates[j]])
                j+=1

        backtrack(target,0,[])
        return res_list
