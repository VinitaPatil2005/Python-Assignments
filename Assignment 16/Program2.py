# Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.
# Input : 11        Output : Odd Number
# Input : 9         Output : Even Number

def ChkNum(number):
    if number%2 == 0:
        return True
    return False

def main():
    Number = int(input("Enter number : "))
    if(ChkNum(Number)):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()