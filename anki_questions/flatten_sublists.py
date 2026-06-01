
k1=[[1,2,3],[4,5],[6],7]

l2 = [x for item in k1 for x in (item if isinstance(item,list) else [item])]
print (l2)