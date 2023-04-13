import random as R
import turtle as t

score=0
playing=False


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

def start():
    global playing
    if playing==False:
        playing=True
        t.clear()
        play()

def play():
    global score
    global playing
    t.fd(10)
    if R.randint(1,5)==3:
        ang=te.towards(t.pos())
        te.seth(ang)
    speed=score+5

    if speed>15:
        speed=15
    te.fd(speed)
    if t.distance(te)<12:
        text="Score: "+str(score)
        message("Game Over",text)
        playing=False
        score=0
    if t.distance(ts)<12:
        score=score+1
        t.write(score)
        star_x=R.randint(-230,230)
        star_y=R.randint(-230,230)
        ts.goto(star_x,star_y)
    if playing:
        t.ontimer(play,100)

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))
    t.home()
    
t.title("Turtle Run")    
t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")
t.listen()

message("Turtle Run","[Space]")
