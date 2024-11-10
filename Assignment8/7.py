class Package:
    def __init__(self, package_id, destination, weight):
        self.package_id = package_id
        self.destination = destination
        self.weight = weight
        self.status = "pending"  

    def deliver(self):
        self.status = "delivered" 

    def __repr__(self):
        return f"Package({self.package_id}, {self.destination}, {self.weight}kg, {self.status})"


class Vehicle:
    def __init__(self, vehicle_id, capacity):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_packages = []

    def load_package(self, package):
        total_weight = sum(p.weight for p in self.current_packages) + package.weight
        if total_weight <= self.capacity:
            self.current_packages.append(package)
        else:
            print(f"Cannot load package {package.package_id}. Capacity exceeded!")

    def deliver_packages(self):
        for package in self.current_packages:
            package.deliver()
        print(f"{self.__class__.__name__} {self.vehicle_id} delivered {len(self.current_packages)} packages.")
        self.current_packages = []  


class Truck(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 1000)  


class Drone(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 10)  

    def load_package(self, package):
        if package.weight > 5:
            raise ValueError(f"Drone cannot carry package {package.package_id} - exceeds 5kg limit!")
        super().load_package(package)


class DeliverySystem:
    def assign_vehicle(self, vehicle, packages):
        for package in packages:
            try:
                vehicle.load_package(package)
            except ValueError as e:
                print(e)

    def dispatch(self, vehicles):
        for vehicle in vehicles:
            vehicle.deliver_packages()
            yield vehicle  
            

def main():
    packages = [
        Package(1, "Location A", 500),
        Package(2, "Location B", 200),
        Package(3, "Location C", 3),
        Package(4, "Location D", 6), 
    ]

    truck = Truck("T-100")
    drone = Drone("D-200")

    delivery_system = DeliverySystem()

    delivery_system.assign_vehicle(truck, packages[:2])
    delivery_system.assign_vehicle(drone, packages[2:])  

    for vehicle in delivery_system.dispatch([truck, drone]):
        pass

    for package in packages:
        print(package)


if __name__ == "__main__":
    main()