from Product_machine import Products
from Product_machine import get_color
from colorist import ColorHex

for x,obj in Products.items():
    print(x,obj)

def main():
    while True:
        try:
            number = int(input("\nChoose the product number: "))  

            if number in Products:
                print(f"You selected: {get_color(number)}{Products[number]['product']}{get_color(0)}, \nCost: € {get_color(number)}{Products[number]['cost']}{get_color(0)}")
                break
            else:
                raise ValueError

        except ValueError:
            print(f"{ColorHex("DC143C")}Invalid command. Please enter a number between 1 and 10.{get_color(0)}")    
    
    purchased = False
    while True:
        if purchased == False:
            amount = input("\nPlease enter the amount to purchase the product (`exit` to cancel transaction): ")
        else: 
            break

        if amount.lower() == 'exit':
            print(f"{ColorHex("191970")}Purchase cancelled.{get_color(0)}")
            break
        
        if amount.lower() != 'exit':
            try:
                amount = float(amount)
        
                while purchased == False:
                    if amount == Products[number]['cost']:
                        print(f"{get_color(number)}Your purchase is confirmed. \nThank you and have a great day! :D{get_color(0)}")
                        purchased = True                        
                        break
        
                    elif amount > Products[number]['cost']:
                        change = amount - Products[number]['cost']
                        print(f"Your purchase is confirmed. \nYour change is € {get_color(number)}{round(change, 2)}{get_color(0)}. \nThank you and have a great day! :D")
                        purchased = True
                        break
        
                    else:
                        to_be_paid = Products[number]['cost'] - amount
                        print(f"The remaining amount is € {get_color(number)}{round(to_be_paid, 2)}{get_color(0)}.")
        
                        while to_be_paid != 0:
                            amount = float(input("Amount: "))
        
                            if amount == to_be_paid:
                                print(f"{get_color(number)}Your purchase is confirmed. \nThank you and have a great day! :D{get_color(0)}")
                                purchased = True
                                break
        
                            elif amount > to_be_paid:
                                change = amount - to_be_paid
                                print(f"Your purchase is confirmed. \nYour change is € {get_color(number)}{round(change, 2)}{get_color(0)}. \nThank you and have a great day! :D")
                                purchased = True
                                break
        
                            else:
                                to_be_paid -= amount
                                print(f"The remaining amount is € {get_color(number)}{round(to_be_paid, 2)}{get_color(0)}.")    
                                                                        
            except ValueError:
                print(f"{ColorHex("DC143C")}Invalid command. Please enter a valid amount or type 'exit' to cancel the transaction.{get_color(0)}")

    
if __name__ == "__main__":
    main()