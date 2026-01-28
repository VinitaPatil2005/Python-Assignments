"""
Design a python application that creates two threads named EvenFactor and OddFactor

- Both threads should accept one integer number as a parameter.
- The EvenFactor thread should:
    > Identify all even factors of the given number.
    > Calculate and display the sum of even factors.
- The OddFactor thread should:
    > Identify all odd factors of the given number.
    > Calculate and display the sum of odd factors.
- After both threads complete execution, the main thread should display the message :
    "Exit from main"

"""

import threading

def EvenFactor(Num):
    EvenSum = 0
    for i in range(2,Num,2):
        if(Num % i == 0):
            EvenSum = EvenSum + i
    print("Sum of Even Factors : ",EvenSum)

def OddFactor(Num):
    OddSum = 0
    for i in range(1,Num,2):
        if(Num % i == 0):
            OddSum = OddSum + i
    print("Sum of Odd Factors : ",OddSum)

def main():
    
    print("Start of main")

    EvenThread = threading.Thread(target=EvenFactor,args=(12,))
    OddThread = threading.Thread(target=OddFactor,args=(15,))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()