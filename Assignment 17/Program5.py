# Write a program which accept one number for user and check whether number is prime or not.

def IsPrime(No):
    for i in range(2, No):
        if (No % i) == 0:
            return False
        
    return True

def main():
    Value = int(input("Enter number : "))

    if IsPrime(Value):
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__ == "__main__":
    main()