# 5. Write a program which accepts marks and displays grade.
#Condition Example:
#≥ 75 → Distinction
#≥ 60 → First Class
#≥ 50 → Second Class
#< 50 → Fail

def determine_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"
    
def main(): 
    try:
        marks = float(input("Enter the marks: "))

        if marks < 0 or marks > 100:
            print("Please enter valid marks between 0 and 100.")
            return
        
        grade = determine_grade(marks)

        print(f"The grade is: {grade}")

    except ValueError:
        print("Invalid input. Please enter numeric marks.")

if __name__ == "__main__":
    main()