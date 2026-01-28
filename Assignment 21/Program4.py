"""
Design a python application that creates two threads.

- Thread 1 should compute the sum of elements from a list.
- Thread 2 should compute the product of elements from the same list.
- Return the results to the main thread and display them.

"""

import threading


def compute_sum(numbers, result, index):
    total = sum(numbers)
    result[index] = total
def compute_product(numbers, result, index):
    product = 1
    for num in numbers:
        product *= num
    result[index] = product

def main():
    numbers = [1, 2, 3, 4, 5]
    result = [0, 0]  

    sum_thread = threading.Thread(target=compute_sum, args=(numbers, result, 0))
    product_thread = threading.Thread(target=compute_product, args=(numbers, result, 1))


    sum_thread.start()
    product_thread.start()

    
    sum_thread.join()
    product_thread.join()

    print(f"Sum of elements: {result[0]}")
    print(f"Product of elements: {result[1]}")

if __name__ == "__main__":
    main()