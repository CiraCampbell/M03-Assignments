# super class
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doorCount, roof):
        Vehicle.__init__(self, vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doorCount = doorCount
        self.roof = roof
    def __str__(self):
        return "Vehicle type: " + self.vehicleType + "\nYear: " + self.year + "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: " + self.doorCount + "\nType of roof: " + self.roof
if __name__ == "__main__":
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doorCount = input("Enter number of doors (2 or 4?): ")
    roof = input("Enter type of roof (solid or sun?): ")
    carObject = Automobile("car", year, make, model, doorCount, roof)
    print("Thanks!")
    print("The details you provided are: ")
    print(carObject)