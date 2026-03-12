num1 = int(input("Enter first number :"))
num2 = int(input("Enter Second number :"))

operation = input("Enter a operations(+ , - , * , / ) : ")

if operation == '+':
    print("Addition is :",num1+num2)
    
elif operation == '-':
    print("Substraction is :",num1-num2)
    
elif operation == '*':
    print("Multiplication is :",num1*num2)
    
elif operation == '/':
    if num1 < num2 or num1 == 0:
        print("Division not possible")
        print("plz enter first number is larger as second number.....")
    else:
        print("Division is :",num1/num2)
        
else:
    print("Enter a correct operations to perform the calculation....")