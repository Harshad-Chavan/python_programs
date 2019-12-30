#https://www.youtube.com/watch?v=DxVPN1PIuLM

import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("snake game by @harshad")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)



# functions
def go_up():
    head.direction = "up"

def go_up():
    head.direction = "up"
def go_down():
        head.direction = "down"
def go_left():
       head.direction = "left"
def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")


# main_game_loop
while True:
    wn.update()
    if head.distance(food) < 20:
        #move the food to a random
        food.goto(x=random.randint(-290,290), y=random.randint(-290,290))


    move()
    time.sleep(delay)

wn.mainloop()
