# Write a program which accept number from user and print number of "*" on screen

def printStar(Num):
    for i in range(5):
        print("*",end="\t")
    
def main():
    No = int(input("Enter the number : "))
    printStar(No)

if __name__ == "__main__":
    main()