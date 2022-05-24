a=[[2,4,6],[8,5,1]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)
# i=0
# c=b[i]
# while i<len(b):
#     if b[i]<c:
#         c=b[i]
#     i=i+1
# print(c)

    