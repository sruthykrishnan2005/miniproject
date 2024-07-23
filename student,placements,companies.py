students = []
placements = []
companies = []

# Function to add a student to the system
def add_student(name, roll_number, department):
    student = {
        'name': name,
        'roll_number': roll_number,
        'department': department
    }
    students.append(student)
    print(f"Student {name} added successfully.")

# Function to add a company to the system
def add_company(name, industry):
    company = {
        'name': name,
        'industry': industry
    }
    companies.append(company)
    print(f"Company {name} added successfully.")

# Function to record placement details
def record_placement(roll_number, company_name, package):
    for student in students:
        if student['roll_number'] == roll_number:
            placement = {
                'roll_number': roll_number,
                'company_name': company_name,
                'package': package
            }
            placements.append(placement)
            print(f"Placement details recorded for student with roll number {roll_number}.")
            return
    print(f"Student with roll number {roll_number} not found.")

# Function to display all students
def display_students():
    print("\nList of Students:")
    for student in students:
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Department: {student['department']}")

# Function to display all companies
def display_companies():
    print("\nList of Companies:")
    for company in companies:
        print(f"Name: {company['name']}, Industry: {company['industry']}")

# Function to display all placements
def display_placements():
    print("\nList of Placements:")
    for placement in placements:
        print(f"Roll Number: {placement['roll_number']}, Company Name: {placement['company_name']}, Package: {placement['package']}")