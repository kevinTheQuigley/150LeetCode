class Solution:
    # Time: O(?)
    # Space: O(?)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # I feel like one would begin by sorting the intervals by the starting value
        intervals.sort(key=lambda x:x[0])
        i=1
        current_interval=intervals[0]
        res = []

        if len(intervals)==1:
            return intervals

        while i<len(intervals):
            if current_interval[1]>=intervals[i][0]:
                current_interval[1] = max(current_interval[1],intervals[i][1])
            else:
                res.append(current_interval)
                current_interval = intervals[i]
            if i==len(intervals)-1:
                res.append(current_interval)
            i+=1

        return res
