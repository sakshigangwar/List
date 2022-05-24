binary_number = [1, 0, 0]
sum=0
i=0
while i<len(binary_number):
    a= binary_number[-i-1]
    sum=sum+a*(2**i)  
    i+=1
print(sum)                                                                 

# binary_number = [1, 0, 0, 2, 1]
# sum=0
# i=0
# while i<len(binary_number):
#     a=binary_number[-i-1]
#     sum=sum+a*(2**i)
#     i=i+1
# print()


# binary_number = [1, 0, 0,"1", 1]
# binary_number=int(binary_number[3])
# print(a)
# sum=0
# i=0
# while i<len(binary_number):
#     b=binary_number[-i-1]
#     sum=sum+b*(2**i)
#     i=i+1
# print(sum)



