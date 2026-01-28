# Write a program which contains filter(), map(), and reduce() in it. python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

from functools import reduce

IsEven = lambda x : x % 2 == 0

Square = lambda x : x*x

Add = lambda x,y : x + y

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    
    # # (for space seperated input)
    # lst = input("Enter Elements : ").split()
    # lst = [int(x) for x in lst]

    for i in range(N):
        value = int(input("Enter element {} : ".format(i+1)))
        lst.append(value)

    FData = list(filter(IsEven,lst))
    print("List after filter : ",FData)

    MData = list(map(Square,FData))
    print("List after map : ",MData)

    RData = reduce(Add,MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()