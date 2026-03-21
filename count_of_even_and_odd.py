      
num = int(input("Enter a Number: "))

counteven = 0
countodd = 0

while num > 0:
    digit = num % 10   # extract last digit

    if digit % 2 == 0:
        counteven += 1
    else:
        countodd += 1

    num = num // 10    # remove last digit

print("Even digits:", counteven)
print("Odd digits:", countodd)