
li = [1,2,3,4,4]

s = set()

[item for item in li if (not item in s) else (s.add(item))]