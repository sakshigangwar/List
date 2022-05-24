a=["mom","nitin","shanvi","madam","sakshi"]
i=0
n=[]
s=[]
while i<len(a):
    str=a[i]
    c=""
    j=1
    while j<len(a[i])+1:
        c=c+a[i][-j]
        j=j+1
    if str==c:
        n.append(str)
    else:
        s.append(a[i])
    i=i+1
print(n)
print(s)

