n1 = int(input())
n2 = int(input())

print("Common Divisors are :",end=" ")
for i in range(1,(n1+1 and n2+1)):
    if(n1%i==0 and n2%i==0):
        gcd=i
        print(gcd,end=" ")

