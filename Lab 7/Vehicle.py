class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = str(vid)
        self.model = str(model)
        self.year = int(year)

    def __str__(self):
        return "VID: " + str(self.vid) + " | " + str(self.model) + " (" + str(self.year) + ")"

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vid == other.vid
        return False

    def is_new(self, n):
        return (2026 - self.year) <= n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = str(fuel_type)
        self.doors = int(doors)

    def __str__(self):
        return "[Car] VID: " + str(self.vid) + " | " + str(self.model) + " (" + str(self.year) + ") | Fuel: " + str(
            self.fuel_type) + " | " + str(self.doors) + " Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return "[Truck] VID: " + str(self.vid) + " | " + str(self.model) + " (" + str(self.year) + ") | Load: " + str(
            self.max_load) + "kg | " + str(self.axles) + " Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type_):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.type = str(type_)

    def __str__(self):
        return "[Motorcycle] VID: " + str(self.vid) + " | " + str(self.model) + " (" + str(
            self.year) + ") | Eng: " + str(self.engine_cc) + "cc | Type: " + str(self.type)


def save_fleet_to_file(vehicles, filename):
    with open(filename, 'w') as file:
        for v in vehicles:
            if isinstance(v, Car):
                file.write(
                    "Car," + str(v.vid) + "," + str(v.model) + "," + str(v.year) + "," + str(v.fuel_type) + "," + str(
                        v.doors) + "\n")
            elif isinstance(v, Truck):
                file.write(
                    "Truck," + str(v.vid) + "," + str(v.model) + "," + str(v.year) + "," + str(v.max_load) + "," + str(
                        v.axles) + "\n")
            elif isinstance(v, Motorcycle):
                file.write("Motorcycle," + str(v.vid) + "," + str(v.model) + "," + str(v.year) + "," + str(
                    v.engine_cc) + "," + str(v.type) + "\n")


def load_fleet_from_file(filename):
    reconstructed_vehicles = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if not parts or len(parts) < 2:
                    continue

                v_type = parts[0]
                if v_type == 'Car':
                    reconstructed_vehicles.append(Car(parts[1], parts[2], parts[3], parts[4], parts[5]))
                elif v_type == 'Truck':
                    reconstructed_vehicles.append(Truck(parts[1], parts[2], parts[3], parts[4], parts[5]))
                elif v_type == 'Motorcycle':
                    reconstructed_vehicles.append(Motorcycle(parts[1], parts[2], parts[3], parts[4], parts[5]))
    except FileNotFoundError:
        print("File not found: " + str(filename))

    return reconstructed_vehicles


if __name__ == "__main__":
    initial_fleet = [
        Car("V001", "Tesla Model 3", 2023, "Electric", 4),
        Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
        Truck("T101", "Volvo FH16", 2019, 25000, 6),
        Truck("T102", "Mercedes Actros", 2021, 18000, 4),
        Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
        Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
    ]

    fleet_filename = "fleet.txt"

    save_fleet_to_file(initial_fleet, fleet_filename)

    print("Loading fleet data from '" + str(fleet_filename) + "'...")
    loaded_vehicles = load_fleet_from_file(fleet_filename)
    print(str(len(loaded_vehicles)) + " vehicles loaded successfully.\n")

    print("All Vehicles ---")
    for vehicle in loaded_vehicles:
        print(vehicle)

    print()

    print("Recent Vehicles (Last 4 Years) ---")
    for vehicle in loaded_vehicles:
        if vehicle.is_new(4):
            print(vehicle)

    print()

    print("Electric Cars Only")
    for vehicle in loaded_vehicles:
        if isinstance(vehicle, Car) and vehicle.fuel_type == "Electric":
            print(vehicle)