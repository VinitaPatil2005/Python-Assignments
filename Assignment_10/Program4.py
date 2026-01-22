#4. Write a program which accepts one number and prints all even numbers till that number.
#Input: 10
#Output: 2 4 6 8 10

def print_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i, end=" ")

def main():
    n = int(input("Enter a number to print all even numbers till that number: "))

    if n < 2:
        print("No even numbers available.")
    else:
        print_even_numbers(n)
        
if __name__ == "__main__":
    main()