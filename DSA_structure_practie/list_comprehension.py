'''
List comprehension
Flatten the sublists of a list which contains mixed types 
intervals = [[1,3],[5,8],[6,7],8]

Do it two ways. Once using a for loop and once using a list comprehension

'''

'''

A list comprehension and a ternaury if else statement. 




'''
intervals = [[1,3],[5,8],[6,7],8]
for interval in intervals:
    for i in (interval if (type(interva)=list) else [interval]):
        i



[i for interval in intervals for i in (interval if (type(interval)==list) else [interval])]