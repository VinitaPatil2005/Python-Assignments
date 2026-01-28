# write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input : 11 5          Output : 16


def Add(No1,No2):
    return No1 + No2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    print(Add(No1,No2))

if __name__ == "__main__":
    main()