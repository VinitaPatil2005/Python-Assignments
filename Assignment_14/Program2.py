# 2. Write a lambda function which accepts one number and returns cube of that number.

cube = lambda x: x ** 3

def main():
    try:
        num = float(input("Enter a number to find its cube: "))
        result = cube(num)
        print(f"The cube of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")   

if __name__ == "__main__":
    main()

