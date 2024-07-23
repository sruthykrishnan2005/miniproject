if __name__ == "__main__":
    while True:
        print("\nWelcome to College Placement System with Company Management")
        print("1. Add Student")
        print("2. Add Company")
        print("3. Record Placement")
        print("4. Display Students")
        print("5. Display Companies")
        print("6. Display Placements")
        print("7. Exit")
        
        choice = input("Enter your choice : ")
        
        if choice == '1':
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            department = input("Enter department: ")
            add_student(name, roll_number, department)
        
        elif choice == '2':
            name = input("Enter company name: ")
            industry = input("Enter industry: ")
            add_company(name, industry)
        
        elif choice == '3':
            roll_number = input("Enter student's roll number: ")
            company_name = input("Enter company name: ")
            package = input("Enter package offered: ")
            record_placement(roll_number, company_name, package)
        
        elif choice == '4':
            display_students()
        
        elif choice == '5':
            display_companies()
        
        elif choice == '6':
            display_placements()
        
        elif choice == '7':
            print("Thank you for using the College Placement System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
