# Write a program which accept one number form user and return addition of its factors.

def SumFactors(No):
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i
    return Sum

def main():
    No = int(input("Enter the Number : "))
    print("Sum of Factors : ",SumFactors(No))

if __name__ == "__main__":
    main()