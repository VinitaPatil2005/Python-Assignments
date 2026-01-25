# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

length_greater_than_5 = lambda x: len(x) > 5

def main():
    try:
        strings = input("Enter strings separated by spaces: ")
        str_list = strings.split()
        filtered_list = list(filter(length_greater_than_5, str_list))
        print(f"The strings with length greater than 5 are: {filtered_list}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()