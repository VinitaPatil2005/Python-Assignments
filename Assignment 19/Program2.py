# Write a program which contains one lambda function which accepts two parameters and return its multiplication.

mul = lambda x,y : x*y

def main():
    No1 = int(input("Enter the First number : "))
    No2 = int(input("Enter the Second number : "))
    print(mul(No1,No2))


if __name__ == "__main__":
    main()