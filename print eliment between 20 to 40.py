numbers=[50, 40, 23, 70, 56, 12, 5, 10,22,39, 7]
i=0
c=0
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<40:
        c+=1
    i+=1
print(c)
