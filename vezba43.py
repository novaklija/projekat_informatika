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

def kornjaca():
    t1 = create_turtle('red', 'circle', 'slowest', -500, 500)
    t2 = create_turtle('blue', 'circle', 'slowest', -500, -500)
    t3 = create_turtle('green', 'circle', 'slowest', 500, -500)
    t4 = create_turtle('yellow', 'circle', 'slowest', 500, 500)

kornjaca()
window.exitonclick()

