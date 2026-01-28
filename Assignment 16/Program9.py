# Write a program which display first 10 even numbers on screen.

def FirstTenEven():
    No = 2
    for i in range(10):
        print(No,end="\t")
        No+=2

def main():
    FirstTenEven()

if __name__ == "__main__":
    main() 