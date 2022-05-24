# for i in range(1,11):
#     while i<=100:
#         print(i,end=" ")
#         i=i+10
#     print()





# i=0
# while i<=10:
#     print(i)
#     i=i+1


# a=int(input("enter the number:"))
# i=1
# while i<=a:
#     j=1
#     while j<=10:
#         b=i*j
#         print(i,"*",j,"=",b)
#         j=j+1
#     print()
#     print()
#     i=i+1



# i=int(input("enter the number check for armstrong number"))
# num=i
# sum=0
# while(i>0):
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if num==sum:
#     print("armstrong number")
# else:
#     print("this is not armstrong number")



# # num=int(input("enter number"))
# # a=num
# # i=0
# # while(num>0):
# #     c=num%10
# #     i=i*10+c
# #     num=num//10
# # if(a==i):
# #     print("palindrome number")
# # else:
# #     print("this is not palindrome number")


# " palindrome number"
# num=int(input("enter the number"))
# a=num[::-1]
# print(a)
# i=0
# while i<1:
#     if num==a:
#         print(a,"palindrome")
#     else:
#         print(a,"not palindrome")
#     i=i+1

# s=[[1,2,3],[4,5,6],[7,8,9]]
# a=[]
# b=[]
# c=[]
# i=0
# while i<len(s):
#     j=0
#     while j<len(s[i]):
#         if j==0:
#             a.append(s[i][j])
#         elif j==1:
#             b.append(s[i][j])
#         elif j==2:
#             c.append(s[i][j])
#         j=j+1
#     i=i+1
# print([a,b,c])



# a=["sakshi","vaishali"]
# a.append("anjali")
# print(a)


# a=["sanvi","sakshi","shivi"]
# a.clear()
# print(a)

# a=["sanvi","sakshi","shivi"]
# a.pop(1)
# print(a)

# a=["sanvi","sakshi","neha"]
# a.copy()
# print(a)

# a=["sanvi","sakshi","shivi"]
# a.reverse()
# print(a)

# a=["sakshi","shivi","sanvi"]
# a.remove(a[2])
# print(a)


# a=["sanvi","sakshi","shivi"]
# b=["rahul","nikhil","rohit"]
# a.extend(b)
# print(a)


# a=["sanvi","sakshi","shivi"]
# a.insert(1,"suraj")
# print(a)

# a=["sakshi","sanvi","shivi"]
# x=a.count("sanvi")
# print(x)



# a=[6,4,8,9,3,2,1]
# a.sort()
# print(a)


# a=["skshi","rahul","nikhil"]
# x=a.index("rahul")
# print(x)






# a=[4,5,6,2,5]
# b=[2,4,6]
# b=[]
# i=0
# s=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         s=s+(a[i]+b[i])
#         j=j+1
#     i=i+1    

# print(s) 


#  list=[1,2,3,4,5,6,7,8,9,10,11,12]
# b=[]
# i=0
# c=0
# while i<len(list):
#     b.append(list[i])
#     if c==1:
#         b.append("10")
#         c=c-3
#     c=c+1
#     i=i+1
# print(b)




#  a=["abhi","drc","tyu"]
# i=0
# while i<len(a):
#     print(i,"-",a[i])
#     i=i+1
    
# a=["abhi","drc","tyu"]
# b={}
# i=0
# while i<len(a):
#     b.update({i:a[i]})
#     i=i+1
# print(b)

# a=[1,3,4,7,6]  
# i=0
# count=0
# while i<len(a):
#     if count==1:
#         a[i]=2
#     if count==3:
#         a[i]=5
#     count=count+1
#     i=i+1
# print(a)



# a=[1,3,4,7,6,7,8,9,10]  
# i=0
# count=0
# while i<len(a):
#     if count==4 or count==6 or count==8:
#         a[i]=4
#     count=count+1
#     i=i+1
# print(a)

# a=int(input("enter the number:"))
# i=1
# while i<a:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(i)
#     i+=1
        
# a=["sakshi","vaishali"]
# i=0
# l=[]
# while i<len(a):
#     j=1
#     sum=" "
#     while j<len(a[i]):
#         sum+=a[i]+1
#         j=j+1
#     l.append(sum)
#     i=i+1
# print(l)
        

# # a=[2,3,4,5,6,7]
# # i=0
# # sum=0
# # while i<len(a):
# #     sum=sum+a[i]
# #     i=i+1
# # print(sum)


# # a=2
# # b="kareena"
# # print(a*b)

# a=2
# b=9
# c=b
# b=a
# print(b)


# a=9
# print(type(a))


# a=["n","a","v","g","u","r","u","k","u","l"]
# i=0
# sum=" "
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)



# a=["sakshi","vaishali","anjali","khushbu"]
# i=0
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a[i]):
#         count=count+1
#         j=j+1
#     i=i+1
#     print(count,a[i])



# a=[2,4,6,1,3,5]
# b=[1,2,3,4]
# sum=0   
# for i in a,b:
#     for j in i:
#         sum=sum+j
# print(sum)

# def dect():
#     key=input("entr key::")
#     a={"sakshi":2,"sweety":4,"monika":8}
#     for i,j in a.items():
#         if key==i:
#             return("ok")
#         else:
#             value=input("enter value::")
#             a.update({key:value})
#         return (a)
# print(dect())


# a=["sakshi","mona","sweety","prachi","shivi"]
# i=0
# b={}
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a[i]):
#         count=count+1
#         b.update({a[i]:count})
#         j=j+1
#     i=i+1
# print(b)


# a=[106,208,109,406,609,307,505]
# i=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     d=""
#     j=0
#     while i<len(c[i]):
#         if a[i]=="0":
#             b.append(c[i])
#     i=i+1
# print(b)
#  


# i=0
# while i<10:
#     i=i+1
#     if i==3 or i==6:
#         pass
#     else:
#         print(i)
       
    

# i=1
# while i<=10:
#     print(i)
#     if i==8:
#         break
#     i=i+1

# def name(a,b=8):
#     c=a+b
#     print("add",c)
# name(2)

# i=452
# while i<467:
#     k=i-451
#     print(k)
#     i+=1
  
# num=int(input("enter the number::"))
# i=0
# a=[]
# b=[]
# c=[]
# while i<num:
#     name=input("enter the name")
#     a.append(name)
#     sar_name=input("enter the sar_name")
#     b.append(sar_name)
#     age=input("enter the age")
#     c.append(age)
#     i=i+1
# print(a)
# print(b)
# print(c) 



# date=int(input("enter the today date"))
# month=int(input("enter the current month"))    
# year=int(input("enter the current year"))
# x=str(date)+"/"+str(month)+"/"+str(year)
# if date>=1 and date<31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
#     date+=1
#     print(str(date)+"/"+str(month)+"/"+str(year))
# elif date>=1 and  date<30 and month==4 or month==6 or month==9 or month==11:
#     date+=1
#     print(str(date)+"/"+str(month)+"/"+str(year))
# elif date==30 or date==31 and month>=1 and month<=11:
#     date=1
#     month+=1
#     print(str(date)+"/"+str(month)+"/"+str(year))
# elif month==12 and date==31:
#     date=1
#     month=1
#     year+=1
#     print(str(date)+"/"+str(month)+"/"+str(year))

# elif month==2 and date<28:
#     date+=1 
#     print(str(date)+"/"+str(month)+"/"+str(year))
# elif month==2 and date==28:
#     date=1
#     month+=1
#     print(str(date)+"/"+str(month)+"/"+str(year))
# elif month==2:
#     if year%4==0 and date==29:
#         date=1
#         month+=1
#         print(str(date)+"/"+str(month)+"/"+str(year))
#     elif year%4==0 and date<29:
#         date+=1
#         print(str(date)+"/"+str(month)+"/"+str(year))
#     else:
#         ("wrong input")
# elif month==12 and date==31:
#     date=1
#     month=1
#     year+=1
#     print(str(date)+str(month)+"/"+str(year))


# a=[2,3,4,8,9,12,12]
# num=int(input("enter the number::"))
# i=0
# sum=0
# while i<len(a):
#     if a[i]==num:
#         x=i+1
#         while x<len(a):
#             sum+=a[x]
#             x=x+1
#     i=i+1
# print(sum)

# a=[2,3,4,8,9,12,12]
# num=int(input("enter the number::"))
# sum=0
# for i in a:
#     if i>num:
#         sum+=i
# print(sum)

# a=[2,3,4,8,9,12,12]
# num=int(input("enter the number::"))
# i=0
# sum=0
# while i<len(a):
#     if a[i]>num:
#         sum+=a[i]
#     i=i+1
# print(sum)

# num=int(input("enter the number::"))
# i=0
# a=[]
# while i<num:
#     b={}
#     name=input("enter the name")
#     sar_name=input("enter the sar_name")
#     age=input("enter the age")
#     b.update({"name":name,"sar_name":sar_name,"age":age})
#     a.append(b)
#     i=i+1
# print(a)


# i=0
# while i<10:
#     i=i+1
#     if i==3 or i==6:
#         pass
#     else:
#         print(i)
    
# a=[2,3,4,5,6,7,8]
# num=int(input("enter the number:"))
# i=0
# while i<len(a):
#     if a[i]>num:
#         print(a[i])
#         break
#     i=i+1


# num=[2,4,6,8,10]
# a=0
# i=0
# while i<len(num):
#     if num[i]>a:
#         a=num[i]
#     i=i+1
# print(a)

# num=[2,4,6,8,10]
# i=0
# b=num[0]
# while i<len(num):
#     if num[i]<b:
#         b=num[i]
#     i=i+1
# print(b)



# a=[[1,2,3],[2,3,4],[1,4,6]]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         b.append(sum)
#         j+=1
#     i+=1
# print(b)


# a=[[1,2,3],[2,3,4],[1,4,6]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][0]+a[i][1]+a[i][2])
#         break    
#     i+=1
# print(b)



# a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# sum=0
# d=[]
# while i<len(a):
#     j=0
#     while j<=i-i:
#         sum+=a[i][j]
#         d.append(sum)
#         j=j+1
#     i=i+1
# print(d)

# a=[[1,2,3],[2,3,4],[3,4,5]]
# i=0
# d=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         if j<=1:
#             sum=sum+a[i][j]
#         j=j+1
#     d.append(sum)
#     i=i+1
# print(d)



# # "amorous"----"showing love"
# "contravene"-----"break a law"
# "delusion"------"false belief"
# "cranny"-------"very small holl"
# "demb founded"-------"unable to speak becausenof suprise"
# "consolidation"----"hindi meaning"
# "break a leg"---"all the best "
# "desprate"------"hopeless felling"
# "coordinator"------"gider"
# "that's alright"----""
# "what an idea"-----""
# "dont make excues"----""
# "stop kidding"----""
# "its all your"----""

# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# prod=1
# while i<len(a):
#     if i<5:
#         sum=sum+a[i]
#     else:
#         prod=prod*a[i]
#     i=i+1
# print(sum)
# print(prod)



# a=[1,2,0,3,4,0,0,5,0,6,0,7,0,8]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# i=0
# while i<len(b):
#     c.append(b[i])
#     i=i+1
# print(c)

# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=0
#     while j<=k:
#         print(i,end=" ")
#         j=j+1
#     k=k+2
#     print

a=[[1,2],[3,2],[4,2]]
i=0
sum=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a):
            sum=sum+a[i]
            b.append(sum)
            j=j+1
        i=i+1
print(b)
