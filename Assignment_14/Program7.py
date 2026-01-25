# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

is_divisible_by_5 = lambda x: x % 5 == 0

def main():
    try:
        num = int(input("Enter a number to check if it is divisible by 5: "))
        #result = is_divisible_by_5(num)
        #print(f"The number {num} is {'divisible' if result else 'not divisible'} by 5.")
        print(is_divisible_by_5(num))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":  
    main()