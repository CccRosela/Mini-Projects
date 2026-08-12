from fruit import get_df
from colorist import ColorHex

df = get_df()

def get_fruit_fact(fruit_name, info):
    columns = {
        1: "Serving",
        2: "Calories",
        3: "Protein",
        4: "Carbs",
        5: "Fat",
        6: "Fiber"
    }
    if info == 7:
        return df.loc[df["Food"] == fruit_name]
    else:
        column = columns[info]
        return df.loc[df["Food"] == fruit_name, column].iloc[0]

def main():
    while True:
        try:
            user = input(f"\nWhich Food would you like to know more about?\n{ColorHex('#800020')}('exit' to cancel):{ColorHex.OFF} ")
            if user.lower() == "exit":
                return

            user = user.lower().capitalize()

            if user not in df['Food'].values:
                raise NameError

            break

        except NameError:
            print(
                f"{ColorHex('#800020')}Please enter one of the following foods:{ColorHex.OFF} \n"
                f"  {ColorHex('#B6D0E2')}{df['Food'].tolist()}{ColorHex.OFF}"
                )

    while True:
        try:
            info = input(f'\nInformation on?:\n    {ColorHex("#B6D0E2")}1: "Serving",   2: "Calories",  3: "Protein",   4: "Carbs",   5: "Fat",   6: "Fiber",   7: "All Information" {ColorHex.OFF} \n{ColorHex('#800020')}(`exit` to cancel):{ColorHex.OFF} ')

            if info.lower() == "exit":
                 return

            info = int(info)
            if info < 1 or info > 7:
                raise ValueError

            break

        except ValueError:
            print(f"    {ColorHex('#800020')}Please enter a correct number (1:7)! {ColorHex.OFF}")

    print(f"\n{ColorHex('#023020')}'{user}': {get_fruit_fact(user,info)}{ColorHex.OFF}")
    

if __name__ == "__main__":
    main()