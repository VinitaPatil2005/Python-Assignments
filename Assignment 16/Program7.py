# write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def DivFive(Num):
    if (Num%5==0):
        return True
    return False

def main():
    No = int(input("Enter the number : "))
    print(DivFive(No))

if __name__ == "__main__":
    main()