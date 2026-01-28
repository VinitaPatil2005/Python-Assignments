# 2. Write a Python program to implement a class named Circle with the following requirements:

# The class should contain three instance variables: Radius, Area, and Circumference.

# The class should contain one class variable named PI, initialized to 3.14.

# Define a constructor (__init__) that initializes all instance variables to 0.0.

# Implement the following instance methods:

# Accept() – accepts the radius of the circle from the user.

# CalculateArea() – calculates the area of the circle and stores it in the Area variable.

# CalculateCircumference() – calculates the circumference of the circle and stores it in the Circumference variable.

# Display() – displays the values of Radius, Area, and Circumference.

# Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14

    def __init__(self, radius, area, circumference):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self, radius):
        self.radius = radius

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius
        return self.area
        
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius
        return self.circumference
    
    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Circumference: {self.circumference}")

def main():
    # Example usage:
    circle1 = Circle(0, 0, 0)

    circle1.Accept(5)
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    circle1.Display()

    circle2 = Circle(0, 0, 0)

    circle2.Accept(10)
    circle2.CalculateArea()
    circle2.CalculateCircumference()
    circle2.Display()

if __name__ == "__main__":
    main()