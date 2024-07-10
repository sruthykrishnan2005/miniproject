class Tourist:
    def __init__(self, name, email, tour_name, tour_date):
        self.name = name
        self.email = email
        self.tour_name = tour_name
        self.tour_date = tour_date

# List to store booked tours (in-memory storage for demonstration)
booked_tours = []

print("Welcome to the Tour Booking System")

while True:
    print("\nMenu:")
    print("1. Book a Tour")
    print("2. View Booking Details")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\n=== Book a Tour ===")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        tour_name = input("Enter the tour name: ")
        tour_date = input("Enter the tour date (YYYY-MM-DD): ")

        tourist = Tourist(name, email, tour_name, tour_date)
        booked_tours.append(tourist)

        print("Tour booked successfully.")

    elif choice == '2':
        print("\n=== View Booking Details ===")
        if not booked_tours:
            print("No bookings yet.")
        else:
            for index, tourist in enumerate(booked_tours, start=1):
                print(f"Booking {index}:")
                print(f"Name: {tourist.name}")
                print(f"Email: {tourist.email}")
                print(f"Tour Name: {tourist.tour_name}")
                print(f"Tour Date: {tourist.tour_date}")
                print()

    elif choice == '3':
        print("\n=== Cancel Booking ===")
        if not booked_tours:
            print("No bookings to cancel.")
        else:
            print("\nCurrent Bookings:")
            for index, tourist in enumerate(booked_tours, start=1):
                print(f"{index}. {tourist.name} - {tourist.tour_name} ({tourist.tour_date})")

            cancel_index = int(input("Enter the booking number to cancel: ")) - 1

            if 0 <= cancel_index < len(booked_tours):
                del booked_tours[cancel_index]
                print("Booking canceled successfully.")
            else:
                print("Invalid booking number.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")