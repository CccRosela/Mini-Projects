from fruit import get_df

df = get_df()

def get_fruit_fact(fruit_name):
    if fruit_name in df['Food'].values:
        fact = df.loc[df['Food'] == fruit_name]
        return fact
    else:
        return "Fruit not found"

user = input("Which Fruit would you like to know more about?: ")
print(get_fruit_fact(user.lower().capitalize()))