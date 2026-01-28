# 3. Write a Python program to implement a class named Arithmetic with the following characteristics:

# The class should contain two instance variables: Value1 and Value2.

# Define a constructor (__init__) that initializes all instance variables to 0.

# Implement the following instance methods:

# Accept() – accepts values for Value1 and Value2 from the user.

# Addition() – returns the addition of Value1 and Value2.

# Subtraction() – returns the subtraction of Value1 and Value2.

# Multiplication() – returns the multiplication of Value1 and Value2.

# Division() – returns the division of Value1 and Value2 (handle division by zero properly).

# Create multiple objects of the Arithmetic class and invoke all the instance methods.


class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter Value1: "))
        self.value2 = int(input("Enter Value2: "))

    def Addition(self):
        return self.value1 + self.value2
    
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        # if self.value2 == 0:
        #     return "Error: Division by zero"
        # return self.value1 / self.value2
        try:
            result = self.value1 / self.value2
        except ZeroDivisionError:
            return "Error: Division by zero"
        else:
            return result

def main():
    # Example usage:
    arith1 = Arithmetic()

    arith1.Accept()
    print("Addition:", arith1.Addition())   
    print("Subtraction:", arith1.Subtraction())
    print("Multiplication:", arith1.Multiplication())
    print("Division:", arith1.Division())

    arith2 = Arithmetic()

    arith2.Accept()
    print("Addition:", arith2.Addition())   
    print("Subtraction:", arith2.Subtraction()) 
    print("Multiplication:", arith2.Multiplication())
    print("Division:", arith2.Division())

if __name__ == "__main__":
    main()