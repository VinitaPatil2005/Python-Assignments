# 3. Write a program which accepts one number and checks whether it is perfect number or not.
#Input: 6
#Output: Perfect Number

def check_perfect_number(n):
        sum_factors = 0

        for i in range(1, n):
            if n % i == 0:
                sum_factors += i
        return sum_factors == n

def main():
    try:
        n = int(input("Enter a number: "))
        if check_perfect_number(n):
            print(f"{n} is a Perfect Number")
        else:
            print(f"{n} is not a Perfect Number")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()




# def is_perfect_number(num):
#     if num < 1:
#         return False
#     divisors_sum = sum(i for i in range(1, num) if num % i == 0)
#     return divisors_sum == num

# def main():
#     number = int(input("Enter a number: "))
#     if is_perfect_number(number):
#         print(f"{number} is a Perfect Number")
#     else:
#         print(f"{number} is not a Perfect Number")
        
# if __name__ == "__main__":
#     main()