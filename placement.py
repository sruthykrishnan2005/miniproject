from student import Student
from miniproject.company import Company

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