elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
coun=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        coun=coun+1
    i=i+1
print("sum of even number:",sum)
print("coun of even number",coun)
print("average of even number",sum//coun)
i=0
while i<len(elements):
    if elements[i]%1 or elements[i]%2:
        sum=sum+elements[i]
        coun=coun+1
    i=i+1
print("sum of odd number",sum)
print("coun of odd number",coun)
print("average of odd number",sum//coun)
i=0
sum=0
coun=0
while i<len(elements):
    sum=sum+elements[i]
    coun=coun+1
    i=i+1
print("sum of list",sum)
print("coun of list",coun)
print("average of list",sum//coun)