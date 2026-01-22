# 2. Write a program which accepts one number and prints sum of first N natural numbers.
#Input: 5
#Output: 15

def sum_of_natural_numbers(n):
    # return n * (n + 1) // 2

    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def main():
    n = int(input("Enter a number to calculate the sum of first N natural numbers: "))
    result = sum_of_natural_numbers(n)
    print("Sum of first", n, "natural numbers is:", result)

if __name__ == "__main__":
    main()