class Solution:
    # Time: O(?)
    # Space: O(?)
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        # This seems relatively easy. Begin by iterating over the list. 
        # The first values we should compare the start and end to find out how the new interval
        # will fit in. Then we pick the smaller of the two. 
        # Then we iterate with the larger of the two combined intervals over the list
        # check if the current intervals overlap

        def check_overlap(interval1,interval2):
            if interval1[0]>interval2[0]:
                return check_overlap(interval2,interval1)
            if interval1[1]>=interval2[0]:
                return True
            else:
                return False

        return_intervals=[]

        new_low=new_interval[0]
        new_high=new_interval[1]

        current_interval = intervals.pop(0)
        while current_interval[0]<=new_interval[0]:
            if not check_overlap(current_interval,new_interval):
                return_intervals.append(current_interval)
                current_interval = intervals.pop(0)
            else:
                new_interval = [min(new_interval,current_interval),max(new_interval,current_interval)]
                break

        while intervals:
            current_interval = intervals.pop(0)
            if not check_overlap(current_interval,new_interval):
                if current_interval[0]< new_interval[0]:
                    return_intervals.append(current_interval)
                    return_intervals.append(new_interval)
                else:
                    return_intervals.append(new_interval)
                    return_intervals.append(current_interval)
                return_intervals.extend(intervals)
                return(return_intervals)
            else:
                new_interval = [min(new_interval,current_interval),max(new_interval,current_interval)]
        return_intervals.append(new_interval)
        return(return_intervals)

        


        





        return []
