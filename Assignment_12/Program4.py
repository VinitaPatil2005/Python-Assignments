# 4. Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

def print_numbers(n):
        for i in range(1, n + 1):
            print(i, end=" ")

def main():
    try:
        n = int(input("Enter a number: "))
        print_numbers(n)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()





# def print_numbers(n):
#     numbers = []
#     for i in range(1, n + 1):
#         numbers.append(i)
#     return numbers

# def main():
#     try:
#         n = int(input("Enter a number: "))
#         if n <= 0:
#             print("Please enter a positive integer.")
#             return
#         numbers = print_numbers(n)
#         print("Numbers from 1 to", n, "are:", ' '.join(map(str, numbers)))
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
        
# if __name__ == "__main__":
#     main()