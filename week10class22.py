import turtle as t

t.shape('turtle')
t.speed(10)
for i in range(4):
    t.forward(200) #이동하는 픽셀
    t.right(90) #우회전 각도

t.fillcolor('red')
t.begin_fill()
t.circle(100)
t.end_fill()
t.done()