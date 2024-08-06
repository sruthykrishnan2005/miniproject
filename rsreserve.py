import sqlite3

def setup_database():
    conn = sqlite3.connect('restaurant_reservation.db')
    cursor = conn.cursor()
    
    # Create reservations table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        guests INTEGER NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

setup_database()

def add_reservation(name, date, time, guests):
    conn = sqlite3.connect('restaurant_reservation.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO reservations (name, date, time, guests)
    VALUES (?, ?, ?, ?)
    ''', (name, date, time, guests))
    
    conn.commit()
    conn.close()
    print("Reservation added successfully!")

def view_reservations():
    conn = sqlite3.connect('restaurant_reservation.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM reservations')
    reservations = cursor.fetchall()
    
    conn.close()
    return reservations

def cancel_reservation(reservation_id):
    conn = sqlite3.connect('restaurant_reservation.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
    
    conn.commit()
    conn.close()
    print("Reservation cancelled successfully!")



def main():
    while True:
        print("\nRestaurant Reservation System")
        print("1. Add Reservation")
        print("2. View Reservations")
        print("3. Cancel Reservation")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter your name: ")
            date = input("Enter reservation date (YYYY-MM-DD): ")
            time = input("Enter reservation time (HH:MM): ")
            guests = int(input("Enter number of guests: "))
            add_reservation(name, date, time, guests)
        
        elif choice == '2':
            reservations = view_reservations()
            if reservations:
                print("\nReservations:")
                for res in reservations:
                    print(f"ID: {res[0]}, Name: {res[1]}, Date: {res[2]}, Time: {res[3]}, Guests: {res[4]}")
            else:
                print("No reservations found.")
        
        elif choice == '3':
            reservation_id = int(input("Enter reservation ID to cancel: "))
            cancel_reservation(reservation_id)
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

    main()