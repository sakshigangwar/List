# a=[2,3,7,5,1,7,4,9,]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]>a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j=j+1
#     i=i+1
# print(a)

a=[2,3,7,5,1,6,4,9,]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j=j+1
    i=i+1
print(a)