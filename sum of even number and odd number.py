elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[]
b=[]
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
        a.append(elements[i])
        sum=sum+(elements[i])
    else:
        b.append(elements[i])
        sum1=sum1+elements[i]
    i=i+1
print("evan number",a,":","sum",sum)
print("odd number is",b,":","sum",sum1)

