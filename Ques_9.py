str = "C Is A High Level Programming Language"
count1=0
count2=0
for i in str:
    if(i.islower()):
        count1=count1+1
    if(i.isupper()):
        count2=count2+1
print(count1)
print(count2)

