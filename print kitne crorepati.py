kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

index=0
Crorepati=0
Lakhpati=0
Dilwale=0
while index<len(kitna_paisa_hai):
    a=kitna_paisa_hai[index]
    if a>=10000000:
        Crorepati+=1
    elif a>=100000 and a<=1000000:
        Lakhpati+=1
    else:
        Dilwale+=1
    index+=1
print("crorepati",Crorepati)
print("lakhpati",Lakhpati)
print("dilwale",Dilwale)

