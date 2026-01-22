def Cube(no):
    return no ** 3

def main():
    print("Enter a Number : ")
    value = int(input())
    ret = Cube(value)
    print("Cube of number is :", ret)
    
if __name__ == "__main__":
    main()