class InsufficientError(Exception):
    def __str__(self):
        return f"Quantity of ingredients is not enough to make your coffee.\n"

class NegativeError(Exception):
    def __str__(self):
        return f"You cannot set negative quantities in the machine."
      
class CoffeeMachine():
    def __init__(self, water=100, coffee=500, milk=1000):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    
    @property
    def water(self):
        return self._water
    @water.setter
    def water(self, water):
        if water < 0:
            raise NegativeError()
        self._water = water

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if coffee <0:
            raise NegativeError()
        self._coffee = coffee
    
    @property
    def milk(self):
        return self._milk
    @milk.setter
    def milk(self, milk):
        if milk < 0:
            raise NegativeError()
        self._milk = milk
    
    def make_coffee(self, coffee_type):
        if coffee_type in types_dic.keys():
            if self.water >= types_dic[coffee_type]['water'] and self.coffee >= types_dic[coffee_type]['coffee'] and self.milk >= types_dic[coffee_type]['milk']:
                self.water -= types_dic[coffee_type]['water']
                self.coffee -= types_dic[coffee_type]['coffee']
                self.milk -= types_dic[coffee_type]['milk']
                return ("Your coffee was made!")
            else: 
                raise InsufficientError()
        else:
            raise ValueError
        
    def __str__(self):
        return f"Status:\n  Water= {self.water}\n  Coffee= {self.coffee}\n  Milk= {self.milk}\n"


types_dic = {
    "black" : {"water" : 0, "coffee" : 20, "milk" : 0}, 
    "doppio" : {"water" : 0, "coffee" : 40, "milk" : 0}, 
    "latte" : {"water" : 0, "coffee" : 6, "milk" : 200}, 
    "cappuccino" : {"water" : 0, "coffee" : 30, "milk" : 200},
    "americano" : {"water" : 100, "coffee" : 20, "milk" : 0}, 
    "macchiato" : {"water" : 0, "coffee" : 10, "milk" : 0}, 
    "cafe au lait" : {"water" : 0, "coffee" : 50, "milk" : 100},
    "iced coffee" : {"water" : 10, "coffee" : 80, "milk" : 30}, 
    "cold brew" : {"water" : 10, "coffee" : 80, "milk" : 200} 
}
    

machine1 = CoffeeMachine(water= 300)
print("Welcome!")

while True:
    try: 
        coffee_type = input("What type of coffee would you like?(or `exit`): ").strip().lower()
        
        if coffee_type == 'exit':
            print("Have a nice day!")
            break
        
        print(machine1.make_coffee(coffee_type))
        print(machine1)
    except ValueError:
        print("The machine cannot make this type of coffee. Please pick something else.\n")
    except InsufficientError: #except does not require the creation of an instance
        print(InsufficientError())
