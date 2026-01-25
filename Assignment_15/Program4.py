# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce 

add = lambda x, y: x + y

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        total = reduce(add, num_list)
        print(f"The addition of all elements in the given list is: {total}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()