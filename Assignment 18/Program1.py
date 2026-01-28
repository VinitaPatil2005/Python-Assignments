# Write a program which accept N numbers from user and store it into List. Return addtion of all elements from that List.

def sum_of_elements(list):
    Sum = 0
    for i in list:
        Sum = Sum + i
    return Sum

def main():
    lst = []
    N = int(input("Enter the number of elements :"))
    # Option 1
    # print("Enter List elements : ")
    # for i in range(N):
    #     lst.append(int(input()))

    # Option 2 (for space seperated input)
    lst = input("Enter Elements : ").split()
    lst = [int(x) for x in lst]
    
    print(sum_of_elements(lst))

if __name__ == "__main__":
    main()