from turtle import Turtle , Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(3)


def move_farward():
    timmy.forward(50)
def move_backward():
    timmy.backward(50)
def move_right():
    timmy.right(37)
def move_left():
    timmy.left(37)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
def pen_up():
    timmy.penup()
def pen_down():
    timmy.pendown()
my_screen = Screen()
my_screen.listen()
my_screen.onkey(key = 'w', fun = move_farward)
my_screen.onkey(key = 's', fun = move_backward)
my_screen.onkey(key = 'd', fun = move_right)
my_screen.onkey(key = 'a', fun = move_left)
my_screen.onkey(key = 'e', fun = pen_up)
my_screen.onkey(key = 'q', fun = pen_down)
my_screen.onkey(clear ,'c')
my_screen.title("Avinash's Sketch Book")
my_screen.exitonclick()
