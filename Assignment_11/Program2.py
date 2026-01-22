# 2. Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def count_digits(num):
    # return len(str(abs(num)))
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count 
   
def main():
    number = int(input("Enter a number: "))
    digit_count = count_digits(number)
    print("Count of digits:", digit_count)

if __name__ == "__main__":
    main()