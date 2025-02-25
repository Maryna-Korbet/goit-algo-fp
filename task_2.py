import turtle
import math
import argparse

def draw_tree(branch_length, level):
    if level == 0:
        return

    # Draw the main branch
    turtle.forward(branch_length)

    # Keep the current position and direction
    position = turtle.pos()
    heading = turtle.heading()

    # Left branch
    turtle.left(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)

    # Return to the initial position
    turtle.setpos(position)
    turtle.setheading(heading)

    # Right branch
    turtle.right(90)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)

    # Let's go back
    turtle.setpos(position)
    turtle.setheading(heading)

def main(level):
    screen = turtle.Screen()
    screen.title("Fractal tree of Pythagoras")
    screen.bgcolor("black")

    turtle.speed(0)
    turtle.left(90)  # Turn up
    turtle.up()
    turtle.goto(0, -250)  # Initial position
    turtle.down()
    turtle.color("white")  

    # Draw the tree
    draw_tree(100, level)
    turtle.done()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fractal tree of Pythagoras')
    parser.add_argument('--level', type=int, default=6, help='Level of recursion (default: 6)')
    args = parser.parse_args()

    if args.level < 0:
        print("Level must be non-negative.")
    else:
        main(args.level)