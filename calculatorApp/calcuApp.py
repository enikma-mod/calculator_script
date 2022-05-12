print("Select an operation to perform: ")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

operation = input()

if operation == "1":
    number1 = int((input("Enter the first number: ")))
    number2 = int((input("Enter the Second number: ")))
    print(f"the sum is {int(number1 + number2)}")

elif operation == "2":
    number1 = int((input("Enter the first number: ")))
    number2 = int((input("Enter the Second number: ")))
    print(f"the difference is {int(number1 - number2)}")

elif operation == "3":
    number1 = int((input("Enter the first number: ")))
    number2 = int((input("Enter the Second number: ")))
    print(f"the product is {int(number1 * number2)}")
    

elif operation == "4":
    number1 = int((input("Enter the first number: ")))
    number2 = int((input("Enter the Second number: ")))
    print(f"the quotient is {int(number1 / number2)}")

else:
    print("invalid entry, Try again!")

