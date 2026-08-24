import itertools # used for the method below
import numpy as np
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def find_target(arr, target):
    # i is current loop no. position
    # j is other number in array position
    for i, number in enumerate(arr):
        for j in range(len(arr)):
            if j > i: # to not look at past numbers ( i != j works as well)
                if number + arr[j] == target:
                    return [i, j]
    return 'Target not found'

def main():
  while True:
    try:
        arr = input("Enter your desired array: ")
        arr = arr.split(",")
        empty_array = []
        for a in arr:
            empty_array.append(int(a))

        arr = np.array(empty_array)
        target = int(input("Enter your target array: "))
        break

    except ValueError:
        print("Please enter your array in the format: #,#,#...,#")
  
  print(find_target(arr, target))
    
if __name__ == "__main__":
    main()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Method below works only if numbers are next to each other:
"""
def find_target(arr, target):
  for x, y in itertools.pairwise(arr):
    if x + y == target:
      return [arr.index(x), arr.index(y)]
  return 'Target not found'
  
def main():
  arr = [2,11,7,10,8]
  target = 9
  
  print(find_target(arr, target))

if __name__ == "__main__":
  main()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
