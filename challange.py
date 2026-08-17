# From https://www.freecodecamp.org/learn/daily-coding-challenge/archive
# Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
# Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
# The returned array should have the indices in ascending order.
import itertools # used for the method below

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
    arr = [2,11,7,10,8]
    target = 9
  
    print(find_target(arr, target))
    
if __name__ == "__main__":
    main()

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
