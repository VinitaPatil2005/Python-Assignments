# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

square = lambda x: x * x

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(float, numbers.split()))
        squared_list = list(map(square, num_list))
        print(f"The squares of the given numbers are: {squared_list}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")

if __name__ == "__main__":
    main()