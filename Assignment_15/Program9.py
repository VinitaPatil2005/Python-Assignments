# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce   

product = lambda x, y: x * y

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        product_result = reduce(product, num_list)
        print(f"The product of all elements in the given list is: {product_result}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()