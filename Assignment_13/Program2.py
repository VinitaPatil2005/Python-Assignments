# 2. Write a program which accepts radius of circle and prints area of circle.

import math

def circle_area(radius):
    area = math.pi * radius * radius
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))

    area = circle_area(radius)
    
    print(f"The area of the circle is: {area}") 

if __name__ == "__main__":
    main()