num = int(input("Enter a number : "))
print("Original Number : ")
for i in range(1,num+1):
    print(i ,end=" ")
    
print("\nReverse Number : ")
for i in range(num,0,-1):
    print(i,end = " ")