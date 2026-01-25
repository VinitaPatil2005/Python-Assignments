# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

even = lambda x: x % 2 == 0

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(int, numbers.split()))
        even_list = list(filter(even, num_list))
        print(f"The even numbers from the given list are: {even_list}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()
