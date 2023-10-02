import turtle

t = turtle.Turtle()
t.width(1)

t.begin_fill()
t.left(160)
t.circle(100,100)
t.circle(200,60)
t.circle(40,90)
t.circle(-40,100)
t.circle(40,100)
t.circle(200,30)
t.left(90)
t.circle(-70,150)
t.left(120)
t.circle(160,55)
t.end_fii()

t.right(110)
t.penup()
t.forward(25)
t.pendown()

t.begin_fill()
t.circle(-100,90)
t.right(90)
t.circle(-100,90)
t.end_fill()

t.hideturtle()
turtle.done()
