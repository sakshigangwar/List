
list = [1, 2, 2, 5, 8, 4, 4, 8]
count= 0 #because [1,2,5,8,4] are unique values.
i=0
b=[]
while i<len(list):
    a=list[i] 
    if a not in b:
        b.append(a)
        count=count+1
    i=i+1
print(b)
print(count)



