#1. Write a program which accepts one number and prints multiplication table of that number.
#Input: 4
#Output:
#4 8 12 16 20 24 28 32 36 40

def multiplication_table(n):
    for i in range(1, 11):
        print(n * i, end=" ")

def main():
    n = int(input("Enter a number to generate its multiplication table: "))
    multiplication_table(n)

if __name__ == "__main__":
    main()