n = 5
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print("\r")
