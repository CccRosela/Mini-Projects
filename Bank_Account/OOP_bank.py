class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, n):
        if n >= 0:
            self.balance += n
            return self.balance
            
    def withdraw(self, n):
        self.balance -= n
        return self.balance

    
acc = input("What is your name?: ").strip().capitalize()
user = BankAccount(acc, 0)
# for person in accounts:
  #  if person['name'] == user:
  #      balance = person['balance']
   #     break
    #else:
     #   balance = 0
print("Current Balance:", user.balance)

def main():
    while True:
        try:
            d = input("\nHow much will you deposit?: ").strip().lower() 
            if d == 'exit' :
                print(f"Final Balance: {balance}")
                return
            else: 
                d = int(d)

            user.deposit(d)
            print(f"Balance: {user.balance}")

    while True:
        try:
            w = input("\nHow much will you withdraw?: ").strip().lower()   
            if w == 'exit' :
                print(f"Final Balance: {user.balance}")
                return
            else:
                w = int(w)
            
            if w < 0:
                raise ValueError    
            
            if user.balance >= w:
                user.withdraw(w)
                print(f"Final Balance: {user.balance}")
                break
            else:
                raise ValueError
        
        except ValueError:
            print("Please enter a correct amount or type `exit`.")



if __name__ == "__main__":
    main()
