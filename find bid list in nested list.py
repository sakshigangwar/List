a=[["bbbb"],["bbbbb"],["bbbbbbbb"]]
i=0
max=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if len(a[i][j])>max:
            b=a[i]
            max=len(a[i][j])
        j=j+1
    i=i+1
print(b,max)
