# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

is_odd = lambda x: x % 2 != 0

def main():
    try:
        num = int(input("Enter a number to check if it is odd: "))
        result = is_odd(num)
        print(f"The number {num} is {'odd' if result else 'even'}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()