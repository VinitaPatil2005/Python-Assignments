# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

minimum = lambda x, y: x if x < y else y

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        min_element = reduce(minimum, num_list)
        print(f"The minimum element in the given list is: {min_element}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()