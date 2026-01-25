# 10. Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

even = lambda x: x % 2 == 0

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(int, numbers.split()))
        even_list = list(filter(even, num_list))
        count_even = len(even_list)
        print(f"The count of even numbers from the given list is: {count_even}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()