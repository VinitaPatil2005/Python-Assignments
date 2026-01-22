# 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# Input: 10 20
# Output: 20 is greater

def ChkGreater(No1, No2):
    if No1 > No2:
        print(f"{No1} is greater")
    elif No2 > No1:
        print(f"{No2} is greater")
    else:
        print("Both numbers are equal")

def main():
    print("Enter two numbers:")
    Value1 = int(input())
    Value2 = int(input())
    ChkGreater(Value1, Value2)

if __name__ == "__main__":
    main()