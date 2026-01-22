#5. Write a program which accepts one number and checks whether it is divisible by 3 and 5.
#Input: 15
#Output: Divisible by 3 and 5

def is_divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Divisible by 3 and 5"
    else:
        return "Not divisible by 3 and 5"
    
def main():
    try:
        number = int(input("Enter a number: "))
        result = is_divisible_by_3_and_5(number)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()