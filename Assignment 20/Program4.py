"""
Design a Python application that creates three threads named Small, Capital, and Digits.

- All threads should accept a string as input.
- The Small thread should count and display the number of lowercase characters.
- The Capital thread should count and display the number of uppercase characters.
- The Digits thread should count and display the number of numberic digits.
- Each thread must also display :
    > Thread ID
    > Thread Name

"""

import threading


def Small(string):
    Count = 0
    for c in string:
        if c.islower():
            Count += 1
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : Small Thread")
    print("Number of Small characters : ",Count)

def Capital(string):
    Count = 0
    for c in string:
        if c.isupper():
            Count += 1
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : Upper Thread")
    print("Number of Upper characters : ",Count)

def Digit(string):
    Count = 0
    for c in string:
        if c.isdigit():
            Count += 1
    print("Thread ID : ",threading.get_ident())
    print("Thread Name : Digit Thread")
    print("Number of Digits : ",Count)


def main():
    print("Start of main")

    S_thread = threading.Thread(target=Small,args=("asdfasjlk12349jadnLKLJGDS23joHHDnlsy32hlFDnlj",))
    C_thread = threading.Thread(target=Capital,args=("asdfasjlk12349jadnLKLJGDS23joHHDnlsy32hlFDnlj",))
    D_thread = threading.Thread(target=Digit,args=("asdfasjlk12349jadnLKLJGDS23joHHDnlsy32hlFDnlj",))

    S_thread.start()
    C_thread.start()
    D_thread.start()

    S_thread.join()
    C_thread.join()
    D_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
