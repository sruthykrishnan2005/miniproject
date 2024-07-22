from student import create_student
from company import create_company
from placement import create_placement

def main():
    placement_system = create_placement()

    # Register students
    student1 = create_student(1, 'Alice', 85)
    student2 = create_student(2, 'Bob', 78)
    student3 = create_student(3, 'Charlie', 92)
    
    placement_system.register_student(student1)
    placement_system.register_student(student2)
    placement_system.register_student(student3)

    # Register companies
    company1 = create_company(1, 'TechCorp', 80)
    company2 = create_company(2, 'BizInc', 70)
    
    placement_system.register_company(company1)
    placement_system.register_company(company2)

    # Place students
    placement_system.place_students()

    # Show placement results
    print("\nPlacement Results:")
    placement_system.show_placements()

if __name__ == "__main__":
    main()