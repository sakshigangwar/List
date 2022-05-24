# l=[1,2,3,4,5,6,8]
# count=0
# for i in l:
#     count=count+1
# print(count)

a = [1,2,3,4,5,6,7,8,9,10]
count = 0

while True:
    try:
        if a[count]:
            count += 1
    except IndexError as e:
        break
print(count)



# a=["sakshi","nirdosh"]
# i=0
# while i<len(a):
#     if len(a[i])%2==0:
#         print("its even=",a[i])
#     else:
#         print("its odd=",a[i])
#     i=i+1