# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def reverse_number(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def main():
    number = int(input("Enter a number: "))
    reversed_num = reverse_number(number)
    print("Reversed Number:", reversed_num)

if __name__ == "__main__":
    main()