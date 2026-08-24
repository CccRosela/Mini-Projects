#Rubik's Cube Challenge - https://www.101computing.net/rubiks-cube-challenge/
import turtle, draw
# draw will be another file imported, which is also useful for the visualization of the problem (provided in the link of the problem)
def rotate(array,clockwise):
   n = len(array)
   newArray = [ [ None for y in range(n) ] for x in range(n) ]
 
   for i in range(n):
      for j in range(n):
         if clockwise==True:
            newArray[i][j] = array[n-j-1][i]
         elif clockwise == False:
            newArray[i][j] = array[j][n-i-1]
   
   draw.draw(newArray)
   array = newArray
   
# 2D array representing one face of a Rubik's Cube
array = [[1, 2, 1],
         [5, 4, 3],
         [2, 1, 6]]

draw.draw(array)
turn = input("""Would you like to rotate this grid:
     a) clockwise
     b) anti-clockwise""")

if turn == "a":
   rotate(array,True)
else:
   rotate(array,False)
