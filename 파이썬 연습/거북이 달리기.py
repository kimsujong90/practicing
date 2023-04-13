import random as R
import turtle as t

 
te=t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(1)
te.up()
te.goto(0,200)

ts=t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.seth(0)

def turn_up():
    t.seth(90)

def turn_left():
    t.seth(180)

def turn_down():
    t.seth(270)

def play():
    t.fd(10)
    ang=te.towards(t.pos())
    te.seth(ang)
    te.fd(9)
    score = 0
    if t.distance(ts)<15:
        star_x=R.randint(-230,230)
        star_y=R.randint(-230,230)
        ts.goto(star_x,star_y)
        score += 1
        print(score)
    if t.distance(te) >= 15:
        t.ontimer(play,100)

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()

play()

while True:
    t.color("white")
    t.color("black")
    t.color("yellow")
    t.color("blue")
    


 
 


