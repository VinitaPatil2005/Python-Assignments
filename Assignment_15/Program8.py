# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

divisible_by_3_and_5 = lambda x: x % 3 == 0 and x % 5 == 0

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(int, numbers.split()))
        filtered_list = list(filter(divisible_by_3_and_5, num_list))
        print(f"The numbers divisible by both 3 and 5 are: {filtered_list}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")
        
if __name__ == "__main__":
    main()