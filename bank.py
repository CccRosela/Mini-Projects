import re

accounts = [
    {"name" : "Rosela" , "balance" : 100},
    {"name" : "Dexter" , "balance" : 50},
    {"name" : "Pony" , "balance" : 200},
    {"name" : "Simon" , "balance" : 600},
    {"name" : "Viola" , "balance" : 999}
]

user = input("What is your name?: ").strip().capitalize()
for person in accounts:
    if person['name'] == user:
        balance = person['balance']
        break
    else:
        balance = 0

print("Current Balance:", balance)

def main():
    global balance
    
    while True:
        try:
            d = input("\nHow much will you deposit?: ").strip().lower()
            
            if d == 'exit' :
                print(f"Current Balance: {balance}")
                return
            else: 
                d = int(d)
            
            if d >= 0:
                deposit(d)
                print(f"Balance: {balance}")
                break
            else:
                raise ValueError
        
        except ValueError:
            print("Please enter a correct amount or type `exit`.")
            continue
            
    while True:
        try:
            w = input("\nHow much will you withdraw?: ").strip().lower()   
            
            if w == 'exit' :
                print(f"Final Balance: {balance}")
                return
            else:
                w = int(w)
            
            if w < 0:
                raise ValueError    
            
            if balance >= w:
                withdraw(w)
                print(f"Balance: {balance}")
                break
            else:
                raise ValueError
        
        except ValueError:
            print("Please enter a correct amount or type `exit`.")

def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
