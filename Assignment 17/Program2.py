# Write a program which accept one number and display below pattern.

def PrintPattern(N):
    for i in range(N):
        for i in range(N):
            print("*",end="\t")
        print()
    
def main():
    No = int(input("Enter the number : "))
    PrintPattern(No)

if __name__ == "__main__":
    main()