from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

BG_COLOR = "black"
WIDTH = 1200
HEIGHT = 600


screen = Screen()
screen.bgcolor(BG_COLOR)
screen.setup(WIDTH, HEIGHT)
screen.title("PİNG PONG")

scoreboard = Scoreboard()
paddle_1 = Paddle(((-WIDTH // 2) + 20, 0))
paddle_2 = Paddle(((WIDTH // 2) - 30, 0))

ball = Ball()


turtle = Turtle()
turtle.speed("fastest")
turtle.color("white")
turtle.penup()
turtle.hideturtle()
turtle.goto(0, (-HEIGHT // 2) + 10)
turtle.setheading(90)
turtle.pensize(2)

while turtle.ycor() < (HEIGHT // 2) + 10:
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)


screen.listen()
screen.onkeypress(paddle_1.move_up, "w")
screen.onkeypress(paddle_1.move_down, "s")
screen.onkeypress(paddle_2.move_up, "Up")
screen.onkeypress(paddle_2.move_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()


    if ball.ycor() > (HEIGHT // 2 - 10) or ball.ycor() < (-HEIGHT // 2 + 10):
        ball.bounce_y()


    if (ball.distance(paddle_1) < 50 and ball.xcor() < -530) or (ball.distance(paddle_2) < 50 and ball.xcor() > 530):
        ball.bounce_x()


    if ball.xcor() > (WIDTH // 2 - 10):
        ball.reset_position()
        scoreboard.increase_score_1()


    if ball.xcor() < (-WIDTH // 2 + 10):
        ball.reset_position()
        scoreboard.increase_score_2()

screen.exitonclick()