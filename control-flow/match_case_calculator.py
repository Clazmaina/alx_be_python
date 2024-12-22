def match_case_calculator(num1,operation,num2):
    match operation:
        case'+':
            return num1 + num2
        case'-':
            return num1 - num2
        case '*':
            return num1 * num2
        case'/':
            if num2 == 0:
                print("Error:Division by zero!")
                return None
            else:
                return num1 / num2
        case'_':
            print("Invalid operation. Please use +,-,*, or /.")
            return None

result = match_case_calculator(28,"*",5)
print(f"The result is: {result}")