import turtle as t

t.colormode(255)

def left_click(x, y):
    t.pendown()
    t.goto(x, y)


def right_click(x, y):
    t.penup()
    t.goto(x, y)

def r_keypress():
    t.pencolor(255,0,0)

def g_keypress():
    t.pencolor(0,255,0)

t.onscreenclick(left_click, 1)
t.onscreenclick(right_click, 3)
t.onkeypress(r_keypress, 'r')
t.onkeypress(g_keypress, 'g')
t.shape('turtle')
t.listen()
t.done()
