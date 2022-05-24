a=[["i","f","g"],["i","s"]]
i=0
while i<len(a):
    j=0
    sum=""
    while j<len(a):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print(sum)

