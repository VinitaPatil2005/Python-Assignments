# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce 

maximum = lambda x, y: x if x > y else y

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        max_element = reduce(maximum, num_list)
        print(f"The maximum element in the given list is: {max_element}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()