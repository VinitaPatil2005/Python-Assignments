# 3. Write a program which accepts one number and prints sum of digits.
#Input: 123
#Output: 6

def sum_of_digits(num):
    total = 0
    while num != 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

def main():
    number = int(input("Enter a number: "))
    digit_sum = sum_of_digits(number)
    print("Sum of digits:", digit_sum)

if __name__ == "__main__":
    main()