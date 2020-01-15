def dictionairy():

    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Keys are sorted in alphabetical order by the key  ")
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")

    inv = {v: k for k, v in key_value.items()}
    print("\n")
    print("reverse values of all keys : ", str(inv))

    sum=0
    for i in key_value:
        sum=sum+key_value[i]

    print("Sum of all values are : ",sum)



def main():

    dictionairy()

if __name__ == "__main__":
    main()



