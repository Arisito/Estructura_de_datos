a=[2,7,8,2,1,8,3,3,7,2,1,9]
b=[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)