import turtle

t = turtle.Turtle()
t.shape('turtle')
ts = t.getscreen()
t.speed(0)
t.hideturtle()

def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)


def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()
    
y = 265
ts.tracer(0)

for row in range(28):
    x = -400
    if row < 9:
        clr = "orange"  
    elif row < 18:
        clr = "white"
    else:
        clr = "green"

    for column in range(40):
        draw_rectangle(x, y, 20, 20, clr)
        x = x + 20

    y = y - 20

n_cols = 5
x_val = -60
y_val = 85

for jj in range(n_cols):
    draw_rectangle(x_val, y_val, 20, 20, "blue")
    x_val = x_val + 20

y_val = 85
x_val = -60

for row in range(9):
    draw_rectangle(x_val, y_val, 20, 20, "blue")
    y_val = y_val - 20

x_val = 40
y_val = 85

for row in range(9):
    draw_rectangle(x_val, y_val, 20, 20, "blue")
    y_val = y_val - 20

n_cols = 6
x_val = 40
y_val = -75

for nn in range(n_cols):
    draw_rectangle(x_val, y_val, 20, 20, "blue")
    x_val = x_val -20

t.pencolor("blue")
t.pensize(5)
draw_line(-60, 105, 60, -75)
draw_line(60, 105, -60, -75)
draw_line(0, 105, 0, -75)
draw_line(-60, 15, 60, 15)
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(15)

ts.update()

turtle.mainloop()
