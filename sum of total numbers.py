# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# sum=0
# while i<len(n):
#     sum=sum+n[i]
#     i=i+1
# print(sum)





# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# m=[]
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         a=n[i]+n[j]
#         s=[n[i],n[j]]
#         if number==a:
#             m.append(s)
#         j=j+1
#     i=i+1
# print(m)

number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
a=[]
i=0
while i<len(n):
    j=0
    while j<i:
        if n[i]+n[j]==number:
            a.append([n[i],n[j]])
        j+=1
    i+=1
print(a)

