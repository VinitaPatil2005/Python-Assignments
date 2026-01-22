#Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def print_reverse_numbers(n):
        for i in range(n, 0, -1):
            print(i, end=" ")

def main():
    try:
        n = int(input("Enter a number: "))
        print_reverse_numbers(n)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()


# def print_reverse_numbers(n):
#     numbers = []
#     for i in range(n, 0, -1):
#         numbers.append(i)
#     return numbers  
# def main():
#     try:
#         n = int(input("Enter a number: "))
#         if n <= 0:
#             print("Please enter a positive integer.")
#             return
#         numbers = print_reverse_numbers(n)
#         print("Numbers from", n, "to 1 are:", ' '.join(map(str, numbers)))
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
        
# if __name__ == "__main__":
#     main()