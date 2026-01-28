# Write a program which accept number from user and return number of digits in that number.

def CountDigits(No):
    iCount = 0
    while(No != 0):
        iCount +=1
        No = No//10
    return iCount

def main():
    No = int(input("Enter the Number : "))
    print(CountDigits(No))

if __name__ == "__main__":
    main()