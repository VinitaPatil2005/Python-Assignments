# 1. Write a lambda function which accepts one number and returns square of that number.

square = lambda x: x * x

def main():
    try:
        num = float(input("Enter a number to find its square: "))
        result = square(num)
        print(f"The square of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
if __name__ == "__main__":
    main()