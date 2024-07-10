bookings=[]

while True:
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    print("Welcome")
    break


while True:
    print("1.add a new tourist destination \n 2.book a tour \n 3.view all bookings \n 4.exit \n")

    ch=input("enter your choice:")
    
    if ch=='1':
        name=input("enter the name of the destination:")
        country=input("enter the country:")
        
    elif ch=='2':
        print("\nbook a tour:")
        name=input("enter your name:")
        destination=input("enter the destination you want to book:")
        booking_date = input("Enter the booking date (YYYY-MM-DD): ")
        bookings.append({"name":name,"destination":destination, "booking_date": booking_date})
        print("booking successful\n")
    
    elif ch=='3':
        print("\nall bookings:")
        if len(bookings) == 0:
            print("no booking yet\n")
        else:
            for booking in bookings:
                print(f"Name: {booking['name']}, Destination: {booking['destination']}, Booking Date: {booking['booking_date']}")
            print()

    
    elif ch == '4':
        print("\nExiting the system.")
        break
    
    else:
        print("\nInvalid choice. Please enter a valid option .\n")

