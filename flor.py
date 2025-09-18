from turtle import *

bgcolor("skyblue")
speed(0)
width(2)

# Girasol
def draw_sunflower():
    pu()
    setpos(0, -100)
    pd()
    width(3)
    R, G, B = 1, 1, 0
    for i in range(100):
        begin_fill()
        color((R, G, B))
        circle(80 - i, 50)
        lt(80)
        circle(80 - i, 50)
        rt(150)
        R = max(0, R - 0.0065)
        G = max(0, G - 0.0065)
        B = max(0, B - 0.0065)
        end_fill()

# Tallo
def draw_stem():
    pu()
    setpos(-100, -100)
    pd()
    color("green")
    width(10)
    setheading(270)
    forward(300)

# Hoja
def draw_leaf():
    pu()
    setpos(-120, -150)
    pd()
    color("darkgreen")
    begin_fill()
    circle(20, 90)
    lt(100)
    circle(20, 90)
    end_fill()

# Sol
def draw_sun():
    pu()
    setpos(-250, 180)
    pd()
    color("yellow")
    begin_fill()
    circle(40)
    end_fill()

# Nube
def draw_cloud(x, y):
    pu()
    setpos(x, y)
    pd()
    color("white")
    begin_fill()
    for _ in range(6):
        circle(20)
        pu()
        forward(20)
        pd()
    end_fill()

# OVNI
def draw_ufo():
    pu()
    setpos(150, 150)
    pd()
    color("gray")
    begin_fill()
    circle(40, 90)
    lt(90)
    circle(40, 90)
    end_fill()

    pu()
    setpos(150, 170)
    pd()
    color("blue")
    begin_fill()
    circle(20)
    end_fill()

# Pasto
def draw_grass():
    pu()
    setpos(-500, -500)
    pd()
    color("forestgreen")
    width(1)
    for x in range(-300, 300, 10):
        setpos(x, -280)
        setheading(90)
        forward(20)
        backward(20)

# Avión
def draw_plane():
    pu()
    setpos(100, 250)
    pd()
    color("silver")
    begin_fill()
    setheading(0)
    forward(60)
    left(120)
    forward(20)
    left(120)
    forward(20)
    left(120)
    forward(60)
    end_fill()

    # Alas
    pu()
    setpos(120, 250)
    pd()
    color("gray")
    begin_fill()
    setheading(90)
    forward(15)
    right(90)
    forward(30)
    right(90)
    forward(15)
    end_fill()

# Dibujo completo
draw_sunflower()
draw_stem()
draw_leaf()
draw_sun()
draw_cloud(-100, 100)
draw_cloud(50, 120)
draw_ufo()
draw_grass()
draw_plane()

done()
