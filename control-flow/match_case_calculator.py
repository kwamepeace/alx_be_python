num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
# result = 0


match operation:
    case "+" :
        result = (num_1 + num_2)
        print(f"The result is {result}.")
    case "-" :
        result = (num_1 - num_2)
        print(f"The result is {result}.")
    case "*" :
        result = (num_1 * num_2)
        print(f"The result is {result}.")
    case "/" :
        if num_1 > 0 and num_2 > 0 :
            result = (num_1 / num_2)
            print(f"The result is {result}.")
        if num_2 == 0:
            print("Cannot divide by zero.")
