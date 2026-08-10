# Based on a 24 hour clock (excluding a.m. / p.m.)
def main():
    user = input("What time is it?: ")
    try:
        if convert(user) >= 7 and convert(user) <= 8:
            print("Breakfast time.")
        elif convert(user) >= 12 and convert(user) <= 13: 
            print("Lunch time.")
        elif convert(user) >= 18 and convert(user) <= 19: 
            print("Dinner time.")
        else:
            print("It's not time to eat yet.")
    except TypeError:
        print("Please enter a valid time as numbers. (Formated as: `#:##` or `##:##`)")


    
def convert(time):
    try: 
        hour, minute = time.strip().split(":")

        hour = int(hour)
        minute = int(minute)

        
        if minute > 60 or minute < 0:
             raise ValueError("Please provide a realistic time.")
        if hour > 24 or hour < 0:
             raise ValueError("Please provide a realistic time.")

        minute = minute/60
        return hour+minute

    except ValueError:
        print("Input must be formated either as `#:##` or `##:##` ") 


if __name__ == "__main__":
    main()