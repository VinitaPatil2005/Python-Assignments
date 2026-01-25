# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

is_even = lambda x: x % 2 == 0

def main():
    try:
        num = int(input("Enter a number to check if it is even: "))
        # result = is_even(num)
        #print(f"The number {num} is {'even' if result else 'odd'}.")
        print(is_even(num))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()