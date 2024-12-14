# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery_capacity = battery_capacity 
        
    def get_battery_capacity(self):
        """Encapsulation: Getter for battery capacity"""
        return self.__battery_capacity

    def set_battery_capacity(self, capacity):
        """Encapsulation: Setter for battery capacity"""
        if capacity > 0:
            self.__battery_capacity = capacity
        else:
            print("Battery capacity must be positive!")

    def call(self, number):
        """Simulate making a call"""
        print(f"{self.brand} {self.model} is calling {number}...")

    def send_message(self, number, message):
        """Simulate sending a message"""
        print(f"Sending message to {number}: {message}")


# Derived class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, strap_material):
        super().__init__(brand, model, storage, battery_capacity)
        self.strap_material = strap_material

    def call(self, number):
        """Overriding method: Call through the smartwatch"""
        print(f"{self.brand} {self.model} smartwatch is calling {number} from your wrist!")

    def fitness_tracking(self):
        """Specific functionality for Smartwatch"""
        print(f"{self.brand} {self.model} is tracking your steps and heart rate.")


# Create an instance of Smartphone
phone = Smartphone("Samsung", "Galaxy S23", "256GB", 5000)
print(f"Phone: {phone.brand} {phone.model}, Storage: {phone.storage}, Battery: {phone.get_battery_capacity()}mAh")
phone.call("+123456789")
phone.send_message("+123456789", "Hello from Python!")

# Create an instance of Smartwatch
watch = Smartwatch("Apple", "Watch Series 8", "32GB", 300, "Leather")
print(f"Watch: {watch.brand} {watch.model}, Strap: {watch.strap_material}, Battery: {watch.get_battery_capacity()}mAh")
watch.call("+987654321")  # Demonstrates polymorphism
watch.fitness_tracking()
