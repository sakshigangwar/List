# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# b=[]
# a=0
# while a<len(n):
#     i=n[a]
#     j=0
#     c=0
#     while j<len(n):
#         if n[a]==n[j] and a!=j:
#             c+=1
#         j+=1
#     if c>=1:
#         if i not in b:
#             b.append(i)
#     a=a+1
# print(b)                                    
     

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
b=[]
a=0
while a<len(n):
    if n[a] not in b:
        b.append(n[a])
    a=a+1
print(b)