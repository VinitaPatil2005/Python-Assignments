# 3. Write a program which accepts one number and prints factorial of that number.
#Input: 5
#Output: 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def main():
    n = int(input("Enter a number to calculate its factorial: "))
    result = factorial(n)
    print("Factorial of", n, "is:", result)

if __name__ == "__main__":
    main()