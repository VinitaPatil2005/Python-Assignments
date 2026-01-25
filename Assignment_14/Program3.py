# 3. Write a lambda function which accepts two numbers and returns maximum number.

maximum_number = lambda x, y: x if x > y else y

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = maximum_number(num1, num2)
        print(f"The maximum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()