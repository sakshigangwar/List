num= [2, 1, 5, 2, 9, 8, 6, 4,3]
i=0
a=[]
b=[]
while i<len(num):
    if num[i]%2==0:
        a.append(num[i])
    else:
        b.append(num[i])
    i+=1
print("even",a)
print("odd",b)