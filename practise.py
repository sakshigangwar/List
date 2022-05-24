# obj=open("student.txt","w")
# for i in range(3):
#     value=input("enter the value")
#     obj.write(value)
#     obj.write("\n")
# obj.close()

# obj=open("student.txt","r")
# sakshi=(obj.readlines())
# print(sakshi)

# a={}
# num=int(input("enter the number:"))
# for i in range(num):
#     k=input("enter the k")
#     v=input("enter the v")
#     a.update({k:v})
# print(a)


# a=[2,3,4,5,6,1]
# num=int(input("enter the number:"))
# sum=0
# i=0
# while i<len(a):
#     if a[i]>num:
#         sum+=a[i]
#     i=i+1
# print(sum)


# a=[1,2,3,4,5,6,7,8]
# num=int(input("enter the number::"))
# i=0
# while i<len(a):
#     if a[i]>num:
#         print(a[i])
#         break
#     i=i+1

# a={"a":"sakshi","b":"nirdosh","c":"nilaksh"}
# for i in a:
#     print(i)

# import json
# d={"name": "David", "class": "I", "age": 6, "f": 8.3}
# y=json.dumps(d)
# print(y)

# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }
# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 6)
  
# out_file.close()



# import json
  
# data = {
#     "name": "Satyam kumar",
#     "place": "patna",
#     "skills": [
#         "Raspberry pi",
#         "Machine Learning",
#         "Web Development"
#     ],
#     "email": "xyz@gmail.com",
#     "projects": [
#         "Python Data Mining",
#         "Python Data Science"
#     ]
# }

# with open( "data_file.json" , "w" ) as write:
#     json.dump( data , write )
    
# with open("data_file.json", "r") as read_content:
#     print(json.load(read_content)) 
   


# a={"name":2,"same":4,"hame":6}
# sum=0
# for i in a:
#     sum+=a[i]
# print(sum)


# n=int(input("enter the number:"))
# a={}
# for i in range(1+n): 
#     a[i]=i**2
# print(a,end="")





# a={"1":"sakshi","2":"sanvi"}
# b={"3":"rahul","4":"nikhil"}
# c={"5":"nirdosh","6":"nilaksh"}
# i=0
# d={}
# while i<len(a):
#     d.update(a)
#     d.update(b)
#     d.update(c)
#     i=i+1
# print(d)
    


# num=int(input("enter the number::"))
# i=0
# a=[]
# b=[]
# c=[]
# while i<num:
#     name=input("enter the name:")
#     a.append(name)
#     sar_name=input("enter the sar_name")
#     b.append(sar_name)
#     age=input("enter the age:")
#     c.append(age)
#     i=i+1
# print(a)
# print(b)
# print(c)

# num=int(input("enter the number:"))
# a=[]
# i=0
# while i<num:
#     b={}
#     name=input("enter the name:")
#     sar_name=input("enter the sar_name:")
#     age=input("enter the age:")
#     b.update({"name":"name","sar_name":"sar_name","age":"age"})
#     a.append(b)
#     i=i+1
# print(a)


# current_year=int(input("enter the current_year:"))
# birth_year=int(input("enter the birth_year:"))
# if current_year>birth_year:
#     print(current_year-birth_year)
# elif current_year>birth_year:
#     print(current_year-birth_year)
# else:
#     print("error")

# "practise"

# i=260
# while i<270:
#     k=i-259
#     print(k)
#     i=i+1



# a=["sakshi","pinky","renu"]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a[i]):
#         count=count+1
#         b.append(count)
#         count=count+1
#         j=j+1
#     i=i+1
# print(b)

# a=["sakshi","pinky","renu"]
# b=[]
# i=0
# while i<len(a):
#     s=len(a[i])
#     b.append(s)
    
#     i+=1
# print(b)        
  