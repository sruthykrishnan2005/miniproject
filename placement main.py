from student import create_student
from miniproject.company import create_company
from placement import create_placement

def main():
    placement_system = create_placement()

    # Register students
    student1 = create_student(1, 'manu', 85)
    student2 = create_student(2, 'Boby', 78)
    student3 = create_student(3, 'anu', 92)
    
    placement_system.register_student(student1)
    placement_system.register_student(student2)
    placement_system.register_student(student3)

    # Register companies
    company1 = create_company(1, 'Techno park', 80)
    company2 = create_company(2, 'sfo', 70)
    
    placement_system.register_company(company1)
    placement_system.register_company(company2)

    # Place students
    placement_system.place_students()

    # Show placement results
    placement_system.show_placements()

if __name__ == "__main__":
    main()
	
