        #Inputs
while True:
    num1 = float(input("Enter First Number  "))
    num2 = float(input("Enter Second Number  "))
    operation = input("Choose an operation (+, -, *, /): ")

        #End loop condition
    if operation.lower() == "exit":
        print("Goodbye! 👋")
        break

        #Calculations
    if operation == ("+"):
        result = (num1 + num2)
    elif operation == ("-"):
        result = num1 - num2
    elif operation == ("*"):
        result = num1 * num2
    elif operation == ("/"):
        if num1 == 0:
            result=("You can not divide by 0")
        else:
            result = num1 / num2
    else:
        result = "Invalid operation!"
   
    if isinstance(result, str):
     print(result)  # Print error message if needed
    else:
        print(f"{num1} {operation} {num2} = {result}")

