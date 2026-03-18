num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i % 7 == 0:
        print("Stopping at:", i)
        break
    print(i)