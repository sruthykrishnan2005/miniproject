class Company:
    def __init__(self, company_id, name, min_grade):
        self.company_id = company_id
        self.name = name
        self.min_grade = min_grade

    def __str__(self):
        return f'Company ID: {self.company_id}, Name: {self.name}, Minimum Grade: {self.min_grade}'

def create_company(company_id, name, min_grade):
    return Company(company_id, name, min_grade)