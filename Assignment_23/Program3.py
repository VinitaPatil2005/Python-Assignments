# 3. Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (__init__) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime() – returns True if the number is prime, otherwise returns False.
# ChkPerfect() – returns True if the number is perfect, otherwise returns False.
# Factors() – displays all factors of the number.
# SumFactors() – returns the sum of all factors.
# (You may use this method as a helper in ChkPerfect() if required.)
# Create multiple objects and call all the methods.

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors of {self.Value}: {factors}")

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total
    
def main():
    num1 = Numbers()
    print(f"Is {num1.Value} prime? {num1.ChkPrime()}")
    print(f"Is {num1.Value} perfect? {num1.ChkPerfect()}")
    num1.Factors()
    print(f"Sum of factors of {num1.Value}: {num1.SumFactors()}")

    num2 = Numbers()
    print(f"Is {num2.Value} prime? {num2.ChkPrime()}")
    print(f"Is {num2.Value} perfect? {num2.ChkPerfect()}")
    num2.Factors()
    print(f"Sum of factors of {num2.Value}: {num2.SumFactors()}")

if __name__ == "__main__":
    main()