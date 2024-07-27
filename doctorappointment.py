class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"


# Subclass for Doctor
class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def __str__(self):
        return f"Dr. {self.name}, Age: {self.age}, Specialty: {self.specialty}"


# Subclass for Patient
class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, ID: {self.patient_id}"


# Appointment class
class Appointment:
    def __init__(self, doctor, patient, date_time):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def __str__(self):
        return f"Appointment: {self.doctor} with {self.patient} on {self.date_time}"


# System to manage appointments
class AppointmentSystem:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, doctor, patient, date_time):
        appointment = Appointment(doctor, patient, date_time)
        self.appointments.append(appointment)
        return appointment

    def show_appointments(self):
        for appointment in self.appointments:
            print(appointment)


# Example usage
if __name__ == "__main__":
    # Create doctors
    doc1 = Doctor("Alice Smith", 40, "Cardiologist")
    doc2 = Doctor("Bob Brown", 50, "Neurologist")

    # Create patients
    pat1 = Patient("John Doe", 30, "P001")
    pat2 = Patient("Jane Roe", 25, "P002")

    # Create the appointment system
    system = AppointmentSystem()

    # Book some appointments
    system.book_appointment(doc1, pat1, "2024-08-15 10:00")
    system.book_appointment(doc2, pat2, "2024-08-15 11:00")

    # Show all appointments
    system.show_appointments()


    while True:
        print("\n1. Book Appointment")
        print("2. Cancel Appointment")
        print("3. Show Appointments")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter patient name: ")
            patient_id = input("Enter patient ID: ")
            doctor_name = input("Enter doctor name: ")
            date_time = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
            try:
                appointment = system.book_appointment(doctor_name, patient_name, patient_id, date_time)
                print(f"Booked: {appointment}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            doctor_name = input("Enter doctor name: ")
            date_time = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
            try:
                appointment = system.cancel_appointment(doctor_name, patient_id, date_time)
                print(f"Cancelled: {appointment}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            system.show_appointments()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

