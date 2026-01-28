# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

def MaxOfList(list):
    Max = list[0]
    for i in range(1,len(list)):
        if list[i] >= Max :
            Max = list[i]
        
    return Max

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    
    # (for space seperated input)
    lst = input("Enter Elements : ").split()
    lst = [int(x) for x in lst]
    
    print(MaxOfList(lst))

if __name__ == "__main__":
    main()