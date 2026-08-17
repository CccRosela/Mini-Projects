# Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.
# Return the chain as an array of strings.

def get_food_chain(pairs):
    food_chain = []
    pred = []
    prey = []

    # Separate predators and prey
    for i in range(len(pairs)):
        x, y = pairs[i]
        pred.append(x)
        prey.append(y)

    # Apex Predator
    for p in pred:
        if p not in prey:
            apex = p
            food_chain.append(apex)

    # Go down the chain
    a = apex
    while a in pred:
        for chain in pairs:
            if a == chain[0]:
                a = chain[1]
                food_chain.append(a)
    
    return food_chain

def main():
  arr = [["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]
  print(get_food_chain(arr))

if __name__ == "__main__":
  main()
