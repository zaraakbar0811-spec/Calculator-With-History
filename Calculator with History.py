history = []

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"

while True:
    print("\n1. New Calculation")
    print("2. Show History")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Operator (+,-,*,/): ")
            num2 = float(input("Enter second number: "))

            result = calculate(num1, num2, op)
            print("Result:", result)

            history.append(f"{num1} {op} {num2} = {result}")
        except:
            print("Invalid input!")

    elif choice == "2":
        print("\nCalculation History:")
        for item in history:
            print(item)

    elif choice == "3":
        break