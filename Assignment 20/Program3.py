"""
Design a Python application that creates two threads named EvenList and OddList.

- Both threads should accept a list of integers as input.
- The EvenList thread should:
    > Extract all even elements from the list.
    > Calculate and display their sum.
- The OddList thread should:
    > Extract all odd elements from the list.
    > Calculate and display their sum.
- Threads should run concurrently.

"""

import threading

def EvenList(lst):
    Sum = 0
    for i in lst:
        if i % 2 == 0:
            Sum = Sum + i
    print("Sum of Even from List : ",Sum)

def OddList(lst):
    Sum = 0
    for i in lst:
        if i % 2 != 0:
            Sum = Sum + i
    print("Sum of Odd from List : ",Sum)


def main():

    print("Start of main")
    
    EvenThread = threading.Thread(target=EvenList,args=([23,42,4,21,5,62],))
    OddThread = threading.Thread(target=OddList,args=([23,42,4,21,5,62],))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

    print("Exit from main")


if __name__ == "__main__":
    main()