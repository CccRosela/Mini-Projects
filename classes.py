class Vehicle:
    def __init__(self, model, max_speed, milage):
        self.model = model
        self.max_speed = max_speed
        self.milage = milage

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle model: {vehicle1.model}, Speed: {vehicle1.max_speed}, Milage: {vehicle1.milage}")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length+ self.width)

rect = Rectangle(10, 4)
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return round(avg,2)

s1 = Student("Simon", [55, 95, 72, 80, 87])
print(f"{s1.name}'s Average Grade: {s1.average()}")


class Stock:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return format(self.price * self.quantity, ",")

bitcoin = Stock("Bitcoin",10990.99, 5)
print(f"{bitcoin.name}: {bitcoin.total_value()}")
