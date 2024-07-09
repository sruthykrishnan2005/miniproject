bookings=[]
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
        bookings.append({"name":name,"destination":destination})
        print("booking successful\n")
    
    elif ch=='3':
        print("\nall bookings:")
        if len(bookings) == 0:
            print("no booking yet\n")
        else:
            for booking in bookings:
                print(f"Name: {booking['name']}, Destination: {booking['destination']}")
            print()

    elif ch == '4':
        cancel_name = input("Enter name to cancel booking: ")
        cancel_destination = input("Enter destination to cancel booking: ")
        for booking in bookings:
            found=False
            if booking['name'].lower() == cancel_name.lower() and booking['destination'].lower() == cancel_destination.lower():
                bookings.remove(booking)
                found=True
                print("Booking for {cancel_name} to {cancel_destination} cancelled.\n")
                break
        
        if not found:
            print("Booking not found for {cancel_name} to {cancel_destination}\n")
    
    elif ch == '5':
        print("\nExiting the system.")
        break
    
    else:
        print("\nInvalid choice. Please enter a valid option .\n")

