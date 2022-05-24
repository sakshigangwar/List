a=[1,-2,3,-4,5,-6,7,8,-9,-10]
b=[]
c=[]
i=0
count=0
count1=0
while i<len(a):
    if a[i]<=0:
        count=count+1
        b.append(a[i])
    else:
        count1=count1+1
        c.append(a[i])
    i=i+1
print(b)
print(c)
print(count)
print(count1)

