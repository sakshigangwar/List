a=[2,3,4,5,6,7],[4,3,6],[2,8,6,4]
i=0
count1=0
count2=0
count3=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            count1+=1
        elif i==1:
            count2+=1
        else:
            count3+=1
        j=j+1
    i=i+1
print(count1)
print(count2)
print(count3)

