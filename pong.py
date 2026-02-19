import turtle
# Display Settings
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.title("PONG BY BK")
wn.tracer()

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.penup()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5,stretch_len= 1)
paddle_a.goto(-350,0)
#Move paddle A
def paddle_a_up():
    y =paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
wn.listen()
wn.onkeypress(paddle_a_up,"w")
def paddle_a_down():
    y =paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
wn.listen()
wn.onkeypress(paddle_a_down,"s")
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5,stretch_len= 1)
paddle_b.goto(350,0)
def paddle_b_up():
    y =paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
wn.listen()
wn.onkeypress(paddle_b_up,"Up")
def paddle_b_down():
    y =paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
wn.listen()
wn.onkeypress(paddle_b_down,"Down")
#Ball
ball = turtle.Turtle()
ball.penup()
ball.speed(10)
ball.shape("circle")
ball.color("Red")
ball.goto(0,0)
ball.dx = 2
ball.dy = 2
#main loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Borders placing
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
    #Paddle Hitting
    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor() + 40 and ball.ycor()>paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1
    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor() + 40 and ball.ycor()>paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1
