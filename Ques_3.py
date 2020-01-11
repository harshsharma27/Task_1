n= int(input())
for i in range(2,n):
    flag = 0
    if(n%i==0):
        flag = 1
        break
if(flag == 0):
    print("Prime Number")
else:
    print("Not Prime Number")