# Write a program which accept N numbes from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function whic is part of our user defined module named MarvellousNum. Name of the function from main python file should be ListPrime()

import MarvellousNum

def ListPrime(list):
    Sum = 0
    for i in list:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i
    return Sum

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    
    # (for space seperated input)
    lst = input("Enter Elements : ").split()
    lst = [int(x) for x in lst]

    print(ListPrime(lst))

if __name__ == "__main__":
    main() 