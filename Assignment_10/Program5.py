#5. Write a program which accepts one number and prints all odd numbers till that number.

def print_odd_numbers(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")       
    
def main():
    n = int(input("Enter a number to print all odd numbers till that number: "))

    if n < 1:
        print("No odd numbers available.")
    else:
        print_odd_numbers(n)

if __name__ == "__main__":
    main()