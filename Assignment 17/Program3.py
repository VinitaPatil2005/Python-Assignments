# Write a program which accept one number from user and return its factorial.

def Fact(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact*i
    
    return Fact

def main():
    No = int(input("Enter the number : "))
    print("Factorial : ",Fact(No))

if __name__ == "__main__":
    main()