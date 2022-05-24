n=input("Enter the line:-")
a=list(str(n))
str=""
i=0
while(i<len(a)):
    str=str+a[i]
    i=i+1
p=str.split()    
count=0
count1=0
j=0
while j<len(p):
    l=0
    while(l<len(p[j])):
        if (p[j][l]==p[j][l].upper()):
            count=count+1
        else:
            count1=count1+1
        l=l+1
    j=j+1
print("Capital Letter is",count)
print("Small letter is",count1)
