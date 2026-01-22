#Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num

    #return n == int(str(n)[::-1])

def main():
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    main()