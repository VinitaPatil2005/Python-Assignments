"""
Design a Python application that creates two separate threads named Even and Odd.

- The Even thread should display the first 10 even numbers
- The Odd thread should display the first 10 odd numbers.
- Both threads should execute independently using the threading module.
- Ensure proper thread creation and execution.

"""

import threading

def PrintEven():
    iCount = 2
    for i in range(10):
        print("PrintEven \t: ",iCount)
        iCount += 2

def PrintOdd():
    iCount = 1
    for i in range(10):
        print("PrintOdd \t: ",iCount)
        iCount += 2  


def main():
    
    t1 = threading.Thread(target=PrintEven)
    t2 = threading.Thread(target=PrintOdd)

    t1.start()
    t2.start()  

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
