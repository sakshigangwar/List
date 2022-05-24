Question_list=["what is the capital of India?",
"what is our national fruite?",
"what is our national biard?"]
option=[["delhi","chennai","chandigarh","bhopal"],
["mango","apple","orange","grapes"],
["sparrow","peacock","crow","hen"]]
solution_list=[1,1,2]
option_list=[["1.delhi","4.bhopal"],["2.apple","1.mango"],["3.crow","2.peacock"]]
print("kon khelega crorpati [KBC]")
i=0
sum=0
coun=0
while i<len(Question_list):
    print(Question_list[i])
    j=0
    k=1
    while j<=len(option):
        print(k,".",option[i][j])
        k=k+1
        j=j+1
    num=input("do u want 50 50 life line")
    if num=="yes":
        print("50 50 lifeline...")
        if coun<1:
            print(option_list[i])
            num1=int(input("enter the number"))
            if num1==solution_list[i]:
                sum=sum+1000
                print("your answer is correct")
                print("u win RS/-",sum)
            else:
                print("your answer is wrong")
                break
            coun=coun+1
        else:
            print("you have alredy used your life line")
            m=int(input("enter the number"))
            if m==solution_list[i]:
                print("u answer is right")
                sum=sum+2000
                print("u wine RS/-",sum)
            else:
                print("u answer is wrong")
                print("u win RS/-",sum)
                break
    else:
        k=int(input("enter the number"))
        if k==solution_list[i]:
            print("right answer")
            sum=sum+2500
            print("u win RS/-",sum)
        else:
            print("no chance")
            print("ur answer is wrong")
            break
    i=i+1