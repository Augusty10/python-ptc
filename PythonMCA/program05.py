num=int(input(" Enter your number: "))

if num<=1:
    print(" not prime ")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
        