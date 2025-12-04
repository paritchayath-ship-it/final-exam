class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self,name,address):
        super().__init__(name)
        self.address =address
    def place_order(self,item):
        self.item = item
        return self.item
    
class Driver(Person):
    def __init__(self,name,address,vehicle):
        super().__init__(name,address)
        self.vehicle =vehicle
    def deliver(self,order):
        self.order = order
        print(f"{drivername} is delivering {self.order} to {self.name} using {self.vehicle}")
        drivername = self.name

class DeliveryOrder:
    def __init__(self,customer,item,status=="preparing"):
        self.customer = customer
        self.item = item
        self.status = status
    def assign_driver(self,driver):
        self.driver = driver
    def summary(self):
        return self.driver
if __name__ == "__main__":
    A =Person("Alice")
    B =Person("Bob")
    D =Person("David")
    print(A)
    print(B)
    print(D)
    print()
    print("Order Summary: ")
    item1=Driver("David","")
    print(f"Iteem: Laptop")
    print()
    print("Final Status:")