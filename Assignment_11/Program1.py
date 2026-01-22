#1. Write a program which accepts one number and checks whether it is prime or not.
#Input: 11
#Output: Prime Number

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("Prime Number")
    else:
        print("Not a Prime Number") 
    
if __name__ == "__main__":
    main()