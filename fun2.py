import turtle
turtle.goto(0,0)

UP = 0
direction = None

def up():
    global direction
    print("You pressed the up key.")
    turtle.forward(50)
turtle.onkey(up, "Up")
turtle.listen()


    
    
        
DOWN = 1
def down():
    print('you pressed the down key.')
    turtle.backward(50)
turtle.onkey(down, "Down")
turtle.listen()

LEFT = 2
def left():
    print('you pressed the left key.')
    turtle.left(90)
turtle.onkey(left, 'Left')
turtle.listen()

RIGHT = 3
def right():
    print('you pressed the right key.')
    turtle.right(90)
    
turtle.onkey(right, 'Right')
turtle.listen()
    
