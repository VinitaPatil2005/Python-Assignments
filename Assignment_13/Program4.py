# 4. Write a program which accepts one number and prints binary equivalent.
def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    
    return bin(n).replace("0b", "")

def main():
    try:
        n = int(input("Enter a decimal number: "))
        binary_equivalent = decimal_to_binary(n)
        print(f"The binary equivalent of {n} is: {binary_equivalent}")
    except ValueError as e:
        print(f"Invalid input: {e}")
        
if __name__ == "__main__":
    main()