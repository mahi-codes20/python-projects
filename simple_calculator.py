#simple calculator
#python project
#created by mahi

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose (+, -, *, /): ")

if operation == "+":
    answer = num1 + num2
    print("Answer:", answer)

elif operation == "-":
    answer = num1 - num2
    print("Answer:", answer)

elif operation == "*":
    answer = num1 * num2
    print("Answer:", answer)

elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        answer = num1 / num2
        print("Answer:", answer)

else:
    print("Invalid operator")
	
	

