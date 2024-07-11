class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.services = []

    def add_service(self, service_name, service_date):
        self.services.append({'name': service_name, 'date': service_date})

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")
        print("Service History:")
        for service in self.services:
            print(f"- {service['date']}: {service['name']}")


class ServiceManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, make, model, year):
        vehicle = Vehicle(make, model, year)
        self.vehicles.append(vehicle)

    def schedule_service(self, vehicle_index, service_name, service_date):
        if vehicle_index >= 0 and vehicle_index < len(self.vehicles):
            self.vehicles[vehicle_index].add_service(service_name, service_date)
            print("Service scheduled successfully.")
        else:
            print("Invalid vehicle index.")

    def display_all_vehicles(self):
        for idx, vehicle in enumerate(self.vehicles):
            print(f"Vehicle {idx + 1}: {vehicle.year} {vehicle.make} {vehicle.model}")

    def display_vehicle_info(self, vehicle_index):
        if vehicle_index >= 0 and vehicle_index < len(self.vehicles):
            self.vehicles[vehicle_index].display_info()
        else:
            print("Invalid vehicle index.")

  from vehicle_service import ServiceManager, Vehicle
from data_management import save_data, load_data
from utils import is_valid_date

def main():
    service_manager = ServiceManager()

    # Load existing data if any
    service_manager.vehicles = load_data('vehicles.json')

    while True:
        print("\nWelcome to the Online Vehicle Service Management System")
        print("1. Add Vehicle")
        print("2. Schedule Service")
        print("3. Display All Vehicles")
        print("4. Display Vehicle Information")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            year = int(input("Enter vehicle year: "))
            service_manager.add_vehicle(make, model, year)

        elif choice == '2':
            service_manager.display_all_vehicles()
            vehicle_index = int(input("Enter vehicle index to schedule service: ")) - 1
            if vehicle_index >= 0 and vehicle_index < len(service_manager.vehicles):
                service_name = input("Enter service name: ")
                service_date = input("Enter service date (YYYY-MM-DD): ")
                if is_valid_date(service_date):
                    service_manager.schedule_service(vehicle_index, service_name, service_date)
                else:
                    print("Invalid date format. Use YYYY-MM-DD.")
            else:
                print("Invalid vehicle index.")

        elif choice == '3':
            service_manager.display_all_vehicles()

        elif choice == '4':
            service_manager.display_all_vehicles()
            vehicle_index = int(input("Enter vehicle index to display information: ")) - 1
            service_manager.display_vehicle_info(vehicle_index)

        elif choice == '5':
            save_data(service_manager.vehicles, 'vehicles.json')
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
          