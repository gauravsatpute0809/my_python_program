
    
    
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime number")

else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number")