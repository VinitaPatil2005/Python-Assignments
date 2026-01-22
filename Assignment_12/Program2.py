#Write a program which accepts one number and prints its factors.
#Input: 12
#Output: 1 2 3 4 6 12
def print_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")  

def main(): 
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return
        print_factors(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()