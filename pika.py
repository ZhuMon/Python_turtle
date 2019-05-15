import turtle as t

t.pensize(3)
t.hideturtle()
t.colormode(255)
t.color("black")
t.setup(700,650)
t.speed(10)
t.st()
t.pu()
t.goto(-210,86)
t.pd()

t.seth(85)
t.circle(-100,40)
p_ear = t.pos()
t.circle(-100,10)
t.seth(25)
t.circle(-170,50)



# right ear
t.seth(40)
t.circle(-250,30)
t.begin_fill()
t.circle(-250,22)

t.seth(227)
t.circle(-270,15)
t.end_fill()
t.circle(-270,28)


t.seth(-80)
t.circle(500,30)

t.seth(-50)
p_tail = t.pos()
t.circle(-100,60)
p_body = t.pos()

t.pu()
t.goto(p_tail)
t.pd()

# tail
t.begin_fill()
t.seth(50)
t.fd(27)
t.seth(-50)
t.fd(30)
#
t.seth(-140)
t.fd(30)
t.end_fill()
t.seth(39)

t.fd(72)
t.seth(125)
t.fd(48)
t.seth(40)
t.fd(53)
t.seth(88)
t.fd(45)

t.seth(35)
t.fd(105)
t.seth(105)
t.circle(850,8)
t.seth(215)
t.circle(850,11)
t.seth(280)
t.fd(110)
t.seth(220)
t.fd(50)
t.seth(304)
t.fd(56)

t.pu()
t.goto(p_body)
t.pd()

t.seth(200)
t.circle(-100,45)

t.seth(150)
t.circle(100,45)
p_body1 = t.pos()
t.circle(100,5)

t.pu()
t.goto(p_body1)
t.pd()

t.seth(235)
t.circle(-70,30)
p_leg = t.pos()
t.circle(-70,30)
t.circle(-40,60)
p_last = t.pos()

# leg1
t.pu()
t.goto(p_body)
t.pd()
t.seth(280)
t.circle(-150,20)

t.seth(120)
t.circle(-150,20)

# leg2
t.pu()
t.goto(p_leg)
t.pd()
t.seth(260)
t.fd(40)
t.seth(170)
t.circle(-40,75)

# left body
t.pu()
t.goto(p_last)
t.pd()
t.seth(90)
t.circle(300,30)

t.pu()
t.fd(40)
t.pd()
t.fd(20)
p_hand = t.pos()
t.fd(20)

t.seth(140)
t.circle(-75,45)
t.seth(70)
t.fd(20)

# left face
t.circle(-10,170)
t.seth(290)
t.circle(-30,45)
t.seth(200)
t.fd(20)

# left hand
t.pu()
t.goto(p_hand)
t.pd()

t.seth(200)
t.fd(80)
t.seth(170)
t.fd(10)
t.seth(280)
t.fd(8)
p_finger = t.pos()
t.fd(2)
t.goto(p_finger)
t.seth(200)
t.fd(10)
t.seth(310)
t.fd(10)
t.seth(240)
t.fd(10)
t.seth(350)
t.fd(10)
t.seth(260)
t.fd(10)
t.seth(370)
t.fd(10)
t.seth(-10)
t.fd(120)

# right hand
t.pu()
t.goto(30,10)
t.pd()

t.seth(145)
t.circle(50,160)

t.pu()
t.goto(-45,-30)
t.pd()
t.seth(135)
t.fd(10)
t.seth(25)
t.fd(10)
t.seth(85)
t.fd(15)
t.seth(-25)
t.fd(10)
t.seth(60)
t.fd(8)
t.seth(-50)
t.fd(10)
t.seth(30)
t.fd(10)
t.seth(-80)
t.fd(10)
t.seth(10)
t.fd(5)
t.seth(-100)
t.fd(27)


# right face
t.pu()
t.goto(-40,70)
t.pd()

t.seth(90)
t.circle(20,360)

# mouth
t.pu()
t.goto(-160,80)
t.pd()

t.seth(-10)
t.circle(30,10)
p_mouth = t.pos()
t.circle(30,30)
t.seth(-5)
t.circle(30,40)

t.pu()
t.goto(p_mouth)
t.pd()
t.seth(275)
t.circle(90,40)
t.seth(65)
t.circle(90,25)
p_tongue = t.pos()
t.circle(90,15)

t.pu()
t.goto(p_tongue)
t.pd()
t.seth(220)
t.circle(90,20)

# left eye
t.pu()
t.goto(-170,130)
t.pd()

t.seth(160)
t.begin_fill()
t.circle(8,359)
t.seth(340)
t.circle(-12,359)
t.end_fill()

# right eye
t.pu()
t.goto(-90,140)
t.pd()

t.seth(20)
t.begin_fill()
t.circle(-9,359)
t.seth(200)
t.circle(13,359)
t.end_fill()


# left ear
t.pu()
t.goto(p_ear)
t.pd()
t.seth(90)
t.circle(-250,30)
t.begin_fill()
t.circle(-250,22)
t.seth(270)
t.circle(-270,15)
t.end_fill()
t.circle(-270,28)



# nose
t.pu()
t.goto(-150,90)
t.pd()

t.fd(1)



a = input()
while a != str(1):
    a = input()
