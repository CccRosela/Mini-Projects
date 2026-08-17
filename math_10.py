import random

def get_problem(x,y,operator):
    if operator == '+':
        return(f"Problem: {x}{operator}{y}",x+y)
    elif operator == '-':
        return(f"Problem: {x}{operator}{y}",x-y)
    elif operator == '×':
        return(f"Problem: {x}{operator}{y}",x*y)


def main():
    i = 0
    correct= 0
    
    while i < 10:
        try:
            x = random.randint(1,10)
            y = random.randint(1,10)
            
            op = ['+','-','×']
            choice = random.choice(op)
            
            math = get_problem(x,y,choice)
        
            problem = input(f"\n{math[0]}\n")
            
            if problem == 'exit':
                return
            
            problem = int(problem)
            
            if math[1] == problem:
                correct += 1
            
            i += 1
            
        
        except ValueError:
                print("Please enter an integer or 'exit'.\n")
            
    
    if correct == 10:
        print("\nGreat job! You answered all problems correctly!")
    elif correct == 0:
        print("\nYou have no correct answers, please try again.")
    else:
        print(f"\nYou got {correct}/10 answers right.")

if __name__ == "__main__":
    main()
