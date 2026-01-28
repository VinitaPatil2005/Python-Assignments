# Write a program which contains one lambda function which accepts one parameter and return power of two

power = lambda x : 2**x

def main():
    No = int(input("Enter the number : "))
    print(power(No))


if __name__ == "__main__":
    main()