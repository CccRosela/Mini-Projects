import turtle

# Match each number to a Rubik's Cube colour
def draw(array):
   colours = {
       1: "red",
       2: "white",
       3: "yellow",
       4: "orange",
       5: "green",
       6: "blue",
       7: "purple",
       8: "cyan",
       9: "magenta",
       0: "black",
   }
   
   n = len(array)

   CELL_SIZE = 100

   screen = turtle.Screen()
   screen.bgcolor("grey")

   pen = turtle.Turtle()
   pen.hideturtle()
   pen.speed(0)
   pen.pensize(5)


   def draw_square(x, y, colour):
       """Draw one coloured square with its top-left corner at x, y."""
       pen.penup()
       pen.goto(x, y)
       pen.setheading(0)
       pen.pendown()

       pen.fillcolor(colour)
       pen.pencolor("black")

       pen.begin_fill()

       for _ in range(n+1):
           pen.forward(CELL_SIZE)
           pen.right(90)

       pen.end_fill()


   # Calculate the starting position so the grid is centred
   grid_width = len(array[0]) * CELL_SIZE
   grid_height = len(array) * CELL_SIZE

   start_x = -grid_width / 2
   start_y = grid_height / 2

   # Draw each value in the array as a coloured square
   for row_index in range(len(array)):
       for column_index in range(len(array[row_index])):
           number = array[row_index][column_index]
           if number == None:
              colour = "grey"
           else:
              colour = colours[number]
           
           x = start_x + column_index * CELL_SIZE
           y = start_y - row_index * CELL_SIZE

           draw_square(x, y, colour)

    # turtle.done()