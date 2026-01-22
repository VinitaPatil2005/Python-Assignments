# 1. Write a program which accepts length and width of rectangle and prints area.

def rectangle_area(length, width):
    area = length * width
    return area 

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()