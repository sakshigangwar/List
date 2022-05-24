number = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
secondmax=0
while i<len(number):
    if max<number[i]:
        max=number[i]
    if number[i]<max and number[i]>secondmax:
        secondmax=number[i]
    i=i+1
print(secondmax)



    
        
    
