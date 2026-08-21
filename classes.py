class Vehicle:
    def __init__(self, model, max_speed, milage):
        self.model = model
        self.max_speed = max_speed
        self.milage = milage

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle model: {vehicle1.model}, Speed: {vehicle1.max_speed}, Milage: {vehicle1.milage}")


class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    def check_password(self, enter):
        if self.password == enter:
            return True
        else:
            raise ValueError

u1 = User("Rosela","CatchMeIfYouCan4")
tries = 0

while tries < 4:
    try:
        enter = input("Please Enter your Password: ")
        u1.check_password(enter)

        print(f"Welcome, {u1.user}")
        break
    except ValueError:
        tries += 1
        print("The password was incorrect.\n")


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


class Light:
    def __init__(self):
        self.on = False
    
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
    def status(self):
        if self.on == True:
            self.state = "ON"
            return self.state
        else:
            self.state = "OFF"
            return self.state

    def __str__(self):
        return f"Light is {self.status()}."

light = Light()
print(light)
light.turn_on()
print(light)


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
