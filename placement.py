class student:
    def __init__(self,std_id,name,grade):
        self.std_id=std_id
        self.name=name
        self.grade=grade
    def __str__(self):
        Student:{self.std_id}, Name:{self.name}, Grade:{self.grade}
    def create_student(std_id,name,grade):
        return Student(std_id,name,grade)
    
class company:
    def __init__(self,company_id,name,min_grade):
        self.company_id = company_id
        self.name = name
        self.min_grade = min_grade
    def __str__(self):
        Company:{self.company_id}, Name: {self.name}, Minimum Grade: {self.min_grade}'

def create_company(company_id, name, min_grade):
    return Company(company_id, name, min_grade)

from student import Student
from company import Company

class Placement:
    def __init__(self):
        self.students = []
        self.companies = []

    def register_student(self, student):
        self.students.append(student)

    def register_company(self, company):
        self.companies.append(company)

    def place_students(self):
        for student in self.students:
            for company in self.companies:
                if student.grade >= company.min_grade and not student.placed:
                    student.placed = True
                    print(f'{student.name} has been placed at {company.name}')
                    break

    def show_placements(self):
        for student in self.students:
            print(student)

def create_placement():
    return Placement()
