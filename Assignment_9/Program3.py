
def Square(no):
    return no*no

def main():
    print("Enter a Number : ")
    value = int(input())
    ret = Square(value)
    print("Square of number is :",ret)

if __name__ == "__main__":
    main()