# Create an module named as arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for divsion. All functions accepts two parameters as number and perform the operation. Write on python program which call all the funtions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter ,second number : "))

    print("Addition is : ",Arithmetic.Add(No1,No2))
    print("Substraction is : ",Arithmetic.Sub(No1,No2))
    print("Multiplication is : ",Arithmetic.Mult(No1,No2))
    print("Division is : ",Arithmetic.Div(No1,No2))

if __name__ == "__main__":
    main()