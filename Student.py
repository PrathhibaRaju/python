class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)
        course.add_student(self)

    def __str__(self):
        return f"Student [ID: {self.student_id}, Name: {self.name}]"


class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        course.assign_teacher(self)

    def __str__(self):
        return f"Teacher [ID: {self.teacher_id}, Name: {self.name}]"


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        return f"Course [Code: {self.course_code}, Name: {self.course_name}]"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"School [Name: {self.name}]"

# Example usage
# Create a school
school = School("Parul School")

# Create students
student1 = Student(1, "Prashanth")
student2 = Student(2, "Koushik")

# Add students to the school
school.add_student(student1)
school.add_student(student2)

# Create teachers
teacher1 = Teacher(1, "Mrs. Prathiba")
teacher2 = Teacher(2, "Mr. Bob")

# Add teachers to the school
school.add_teacher(teacher1)
school.add_teacher(teacher2)

# Create courses
course1 = Course("MATH101", "Mathematics")
course2 = Course("SCI101", "Science")

# Add courses to the school
school.add_course(course1)
school.add_course(course2)

# Enroll students in courses
student1.enroll_in_course(course1)
student2.enroll_in_course(course2)

# Assign teachers to courses
teacher1.assign_course(course1)
teacher2.assign_course(course2)

# Print details
print(student1)
print(student2)
print(teacher1)
print(teacher2)
print(course1)
print(course2)
print(school)
