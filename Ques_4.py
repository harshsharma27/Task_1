n1 = int(input())
n2 = int(input())
i=0
while(i<=n1 and i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
    ++i
print(gcd)
