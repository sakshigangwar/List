list=[2,4,6,8,7,1,3,5,9]
j=0
k=[]
c=[]
while j<len(list):
    i=1
    count=0
    while i<=list[j]:
        if list[j]%i==0:
            count=count+1
        i=i+1
    if count==2:
        k.append(list[j])
    else:
        c.append(list[j])
    j=j+1
print("it is prime number",k)
print("it is not prime number",c)




i=1
b=[]
while i<=100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
       b.append(i)
    i=i+1
print(b)         
