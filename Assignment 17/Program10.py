# Write a program which accept number from user and return number of digits in that number.

def SumDigits(No):
    Sum = 0
    while(No != 0):
        Sum = Sum + (No%10)
        No = No//10
    return Sum

def main():
    No = int(input("Enter the Number : "))
    print(SumDigits(No))

if __name__ == "__main__":
    main()