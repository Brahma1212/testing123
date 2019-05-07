duplicates=[1,1,2,2,3,3,4,4,5,6,7]
empty=[]
for i in duplicates:
    if i not in empty:
        empty.add(i)
print(empty)