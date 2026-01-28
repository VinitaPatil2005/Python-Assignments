# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accpeted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce

CheckNum = lambda x : x >= 70 and x <= 90

increase = lambda x : x+10

prod = lambda x,y : x * y

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    
    # (for space seperated input)
    # lst = input("Enter Elements : ").split()
    # lst = [int(x) for x in lst]
    for i in range(N):
        value = int(input("Enter element {} : ".format(i+1)))
        lst.append(value)

    FData = list(filter(CheckNum,lst))
    print("List after filter : ",FData)

    MData = list(map(increase,FData))
    print("List after map : ",MData)

    RData = reduce(prod,MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()