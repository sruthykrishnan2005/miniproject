class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.placed = False

    def __str__(self):
        return f'Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Placed: {self.placed}'

def create_student(student_id, name, grade):
    return Student(student_id, name, grade)