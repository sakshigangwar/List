a=[1,2,3,4,5,6,7,8]
b=[10,20,30,40,50,60]
i=0
j=1
while i<len(a):
    print(a[i]+b[-j])
    j+=1
    i+=1
    