# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def calculate_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = None
    if num2 != 0:
        division = num1 / num2
    return addition, subtraction, multiplication, division  

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        addition, subtraction, multiplication, division = calculate_operations(num1, num2)
        print("Addition:", addition)
        print("Subtraction:", subtraction)
        print("Multiplication:", multiplication)
        if division is not None:
            print("Division:", division)
        else:
            print("Division: Undefined (cannot divide by zero)")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()