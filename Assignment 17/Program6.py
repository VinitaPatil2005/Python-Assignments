# Write a program which accept one number and display below pattern.
# * * * * *
# * * * *
# * * *
# * *
# *

def PrintPattern(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("* ",end="")
        print()

def main():
    No = int(input("Enter the Number : "))
    PrintPattern(No)


if __name__ == "__main__":
    main()