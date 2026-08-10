user = input("Expression: ")

def math_calc(math):
    try:
        parts = math.strip().split()
        if len(parts) != 3:
            raise ValueError("Expression must be in the format of: `number` `operator` `number`. (E.g:1 + 2)")

        x = float(parts[0])
        z = float(parts[2])
        y = parts[1]

        if y == "+":
            print(x+z)
        elif y == "-":
            print(x-z)
        elif y == "*":
            print(x*z)
        elif y == "/":
            print(x/z)
        else:
            raise ValueError("Please only use one of the following operators: +,-,*,/")

    except ZeroDivisionError:
        print("Cannot divide by 0")

math_calc(user)