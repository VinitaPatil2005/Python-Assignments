# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

odd = lambda x: x % 2 != 0  

def main():
    try:
        numbers = input("Enter numbers separated by spaces: ")
        num_list = list(map(int, numbers.split()))
        odd_list = list(filter(odd, num_list))
        print(f"The odd numbers from the given list are: {odd_list}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.") 
           
if __name__ == "__main__":
    main()