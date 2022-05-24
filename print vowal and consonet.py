a=input("enter the name")
i=0
while i<len(a):
    if a[i]=="a" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        print("vowal=",a[i])
    else:
        print("consonent=",a[i])
    i=i+1