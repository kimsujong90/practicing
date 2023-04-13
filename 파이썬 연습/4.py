import turtle as t
t.shape("turtle")

def t_right():
    t.seth(0)
    t.fd(10)

def t_up():
    t.seth(90)
    t.fd(10)

def t_left():
    t.seth(180)
    t.fd(10)

def t_down():
    t.seth(270)
    t.fd(10)

def blank():
    t.clear()

def tail_up():
    t.up()

def tail_down():
    t.down()

t.speed(0)
t.onkeypress(t_right,"Right")
t.onkeypress(t_up,"Up")
t.onkeypress(t_left,"Left")
t.onkeypress(t_down,"Down")
t.onkeypress(blank,"space")
t.onkeypress(tail_up,"z")
t.onkeypress(tail_down,"x")
t.listen()

