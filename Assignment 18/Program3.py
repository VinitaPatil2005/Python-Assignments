# Write a program which accept N numbers from user and store it into List. Return Minimum number from that list.

def MinOfList(list):
    Min = list[0]
    for i in range(1,len(list)):
        if list[i] <= Min :
            Min = list[i]
        
    return Min

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    
    # (for space seperated input)
    lst = input("Enter Elements : ").split()
    lst = [int(x) for x in lst]
    
    print(MinOfList(lst))

if __name__ == "__main__":
    main()