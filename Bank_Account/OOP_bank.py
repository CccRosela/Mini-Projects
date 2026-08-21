class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = balance
    
    def deposit(self, n):
        if n >= 0:
            self.balance += n
            return self.balance
        else:
            raise ValueError
            
    def withdraw(self, n):
        if n >= 0 and self.balance >= n:
            self.balance -= n
            return self.balance
        else:
            raise ValueError

special = BankAccount("Rosela", 1000)
acc = input("What is your name?: ").strip().capitalize()

if acc == special.name:
    user = special
else:
    user = BankAccount(acc, 0)

print("Current Balance:", format(user.balance, ","))

def main():
    while True:
        try:
            d = input("\nHow much will you deposit?: ").strip().lower() 
            if d == 'exit' :
                print(f"Final Balance: {format(user.balance, ",")}")
                return
            else: 
                d = int(d)

            user.deposit(d)
            print(f"Balance: {format(user.balance, ",")}")
            break
        
        except ValueError:
            print("Please enter a correct amount or type `exit`.")
        
    while True:
        try:
            w = input("\nHow much will you withdraw?: ").strip().lower()   
            if w == 'exit' :
                print(f"Final Balance: {format(user.balance, ",")}")
                return
            else:
                w = int(w)

            user.withdraw(w)
            print(f"Final Balance: {format(user.balance, ",")}")
            break
        
        except ValueError:
            print("Please enter a correct amount or type `exit`.")

if __name__ == "__main__":
    main()
