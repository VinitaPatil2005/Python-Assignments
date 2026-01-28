# Write a program which accept number from user and check whether that number is positive or negative or zero.

def SignNumber(Number):
    if(Number > 0):
        print("Positive Number")
    elif(Number < 0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    No = int(input("Enter the number : "))
    SignNumber(No)

if __name__ == "__main__":
    main()
    