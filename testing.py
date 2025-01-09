import heapq
randomNums = [1,5,3,7,9,12,745,3,5,4]
smallNums = []

for num in randomNums:
    heapq.heappush(smallNums,num)
    #if len(smallNums)>3:
    #    heapq.heappop(smallNums)
    print(smallNums)