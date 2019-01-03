import turtle

window = turtle.Screen()
window.setup(1000, 1000)

def create_turtle(boja,oblik,brzina,x,y):
    t2 = turtle.RawTurtle(window)
    t2.color(boja)
    t2.shape(oblik)
    t2.speed(brzina)
    t2.penup()
    t2.setposition(x, y)
    return t2

t1 = create_turtle('red','circle',6,100,40)
t2 = create_turtle('blue','square',10,150,60)
t3 = create_turtle('green','triangle','slowest',190,20)
t2.forward(150)
window.exitonclick()
