# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return maximum number from that numbers. 

import functools

def IsPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

Mult = lambda No : No*2

def Max(No1,No2):
    if No1 >=No2:
        return No1
    return No2

def main():
    lst = []
    N = int(input("Enter the number of elements :"))

    for i in range(N):
        value = int(input("Enter element {} : ".format(i+1)))
        lst.append(value)
    
    FData = list(filter(IsPrime,lst))
    print("List after filter : ",FData)

    MData = list(map(Mult,FData))
    print("List after map : ",MData)

    RData = functools.reduce(Max,MData)
    print("Output of reduce : ",RData)
    

if __name__ == "__main__":
    main()