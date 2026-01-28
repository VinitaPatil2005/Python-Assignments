# Write a program which accpet N numbers from user and into List. Accept one another number from user and return frequency of that number from List.

def FrequencyCount(lst,No):
    iCount = 0

    for i in lst:
        if(i == No):
            iCount+=1
    return iCount

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    
    # (for space seperated input)
    lst = input("Enter Elements : ").split()
    lst = [int(x) for x in lst]

    Ele = int(input("Element to search : "))

    print(FrequencyCount(lst,Ele))

if __name__ == "__main__":
    main() 