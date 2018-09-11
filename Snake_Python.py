#Snake Python Game
#Changed Maxim Shmakov (Chevis)

import turtle
import time
import random

bordersize = 300

delay = 0.1
score = 0
highscore = 0 
leftscore = random.randint(3,8)

#Window
wnd = turtle.Screen()
wnd.title("Snake Python")
wnd.bgcolor("#f8e597") #Background color
wnd.setup(width=bordersize*2,height=bordersize*2)
wnd.tracer(0)

border = turtle.Turtle()
border.penup()
border.goto(-bordersize,-bordersize)
border.speed(10)
border.pendown()
border.pensize(3)
border.color("black")

for side in range(4):
    border.forward(bordersize*2)
    border.left(90)

border.hideturtle()

#Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("#678b5c") #Snake color
snake.penup()
snake.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#db494a") #Food color
food.penup()
food.goto(random.randint(-bordersize + 20,bordersize - 20),random.randint(-bordersize + 20,bordersize - 20))

#Create segments
segments = []

#Write the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier New", 24, "normal"))

#Set Directions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

#Events keyboard
wnd.listen()
wnd.onkeypress(go_up, "w")
wnd.onkeypress(go_down, "s")
wnd.onkeypress(go_left, "a")
wnd.onkeypress(go_right, "d")

#Move snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
#Update
while True:
    wnd.update()

    #Collision with the border
    if snake.xcor()>bordersize - 10 or snake.xcor()<-bordersize + 10 or snake.ycor()>bordersize - 10 or snake.ycor()<-bordersize + 10:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"
        
        for segment in segments:
            segment.hideturtle()

        segments.clear()

        delay = 0.1
        score = 0
        leftscore = random.randint(3,8)

        food.color("#db494a")
        food.turtlesize(1)

        x = random.randint(-bordersize + 20, bordersize - 20)
        y = random.randint(-bordersize + 20, bordersize - 20)
        food.goto(x,y)

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,highscore,), align="center", font=("Courier New", 24, "normal"))

    #Collision with the food
    if snake.distance(food) < 20:
        #Add a segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("#72b573")
        new_segment.penup()
        segments.append(new_segment)

        if leftscore == 0:
            food.color("#db494a")
            food.turtlesize(1)

            #Speed delay
            delay -= 0.002
            #Reset score
            leftscore = random.randint(3,8)
            #Add a score
            score += 50

        else:
            #Speed delay
            delay -= 0.001
            #Add a score
            score += 10

            leftscore -= 1

            if leftscore == 0:
                food.color("#3f48cc")
                food.turtlesize(1.5)
            else:
                food.color("#db494a")
                food.turtlesize(1)

        x = random.randint(-bordersize + 20, bordersize - 20)
        y = random.randint(-bordersize + 20, bordersize - 20)
        food.goto(x,y)

        if score > highscore:
            highscore = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,highscore), align="center", font=("Courier New", 24, "normal"))

    #Moving segments
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)


    #Collision with the segments
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            for segment in segments:
                segment.hideturtle()

            segments.clear()

            delay = 0.1
            score = 0
            leftscore = random.randint(3,8)
            
            food.color("#db494a")
            food.turtlesize(1)

            x = random.randint(-bordersize + 20, bordersize - 20)
            y = random.randint(-bordersize + 20, bordersize - 20)
            food.goto(x,y)

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,highscore), align="center", font=("Courier New", 24, "normal"))

    #Move segments
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)
wnd.mainloop()
