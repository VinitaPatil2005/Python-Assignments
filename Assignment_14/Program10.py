# 10. Write a lambda function which accepts three numbers and returns largest number.

largest = lambda x, y, z: x if (x > y and x > z) else (y if y > z else z)

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        result = largest(num1, num2, num3)
        print(f"The largest of {num1}, {num2}, and {num3} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        
if __name__ == "__main__":
    main()