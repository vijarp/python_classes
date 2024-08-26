"""Create a class Student that models a student’s academic record. The class should have the following features:

Attributes:

name: The name of the student.
roll_number: The roll number of the student.
grades: A dictionary where keys are course names and values are the grades for those courses.
Methods:

add_course(course_name, grade): Adds a course and its grade to the student’s record.
update_grade(course_name, grade): Updates the grade for an existing course.
calculate_gpa(): Calculates and returns the student's GPA. Assume grades are given as letters ('A', 'B', 'C', etc.) and convert them to a GPA on a 4.0 scale (e.g., 'A' = 4.0, 'B' = 3.0, etc.).
print_record(): Prints the student’s name, roll number, and their course list with grades.
Edge Cases:

Handle cases where the course already exists when adding a new course.
Handle invalid grade entries when updating grades.
Handle cases where GPA calculation is attempted with no courses.
GPA Conversion Scale:
'A': 4.0
'B': 3.0
'C': 2.0
'D': 1.0
'F': 0.0"""

class Student:
    def __init__(self, student_name, roll_no):
        self.student_name = student_name
        self.roll_no = roll_no
        self.grades = {}  # Initialize an empty dictionary to store courses and grades

    def add_course(self, course_name, grade):
        if course_name not in self.grades:
            if grade in ['A', 'B', 'C', 'D', 'F']:
                self.grades[course_name] = grade
            else:
                print("Invalid grade. Must be one of A, B, C, D, F.")
        else:
            print(f"Course {course_name} already exists. Use update_grade to change the grade.")

    def update_grade(self, course_name, grade):
        if course_name in self.grades:
            if grade in ['A', 'B', 'C', 'D', 'F']:
                self.grades[course_name] = grade
            else:
                print("Invalid grade. Must be one of A, B, C, D, F.")
        else:
            print(f"Course {course_name} not found. Add the course first using add_course.")

    def calculate_gpa(self):
        if not self.grades:
            print("No courses found. Cannot calculate GPA.")
            return None
        
        # GPA conversion dictionary
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_points = 0.0
        
        for grade in self.grades.values():
            total_points += grade_points[grade]
        
        gpa = total_points / len(self.grades)
        return round(gpa, 2)

    def print_record(self):
        print(f"Student Name: {self.student_name}")
        print(f"Roll Number: {self.roll_no}")
        print("Courses and Grades:")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")

# Example Usage
student1 = Student("John Doe", "12345")

# Add courses and grades
student1.add_course("Math", "A")
student1.add_course("History", "B")

# Update a grade
student1.update_grade("History", "A")

# Print the student's record
student1.print_record()

# Calculate and print the GPA
print(f"GPA: {student1.calculate_gpa()}")  # Output should be the GPA based on the courses and grades
