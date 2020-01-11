str = "I want to learn Python"
str1 = ""

i=0
for x in str:
    if str.index(x)==i:
        str1 = str1+x
    i+=1
print(str1)


