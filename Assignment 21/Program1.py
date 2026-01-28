"""
Design a Python application that creates two threads named Prime and NonPrime.

- Both threads should accept a list of integers.
- The Prime thread should display all prime numbers from the list.
- The NonPrime Thread should display all non-prime numbers from the list.
"""

import threading

def Prime(lst):
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("Prime :",num)

def NonPrime(lst):
    for num in lst:
        if num <= 1:
            print("NonPrime :",num)
        else:
            for i in range(2, num):
                if (num % i) == 0:
                    print("NonPrime :",num)
                    break

def main():
    numbers = [10, 15, 23, 42, 7, 8, 3, 4, 1, 0, -5]

    p_thread = threading.Thread(target=Prime, args=(numbers,))
    np_thread = threading.Thread(target=NonPrime, args=(numbers,))

    p_thread.start()
    np_thread.start()

    p_thread.join()
    np_thread.join()

if __name__ == "__main__":
    main()