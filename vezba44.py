#prva vezba
# import turtle
#
# def prozor(ime):
#     window = turtle.Screen()
#     window.title(ime)
#     window.setup(400, 200)
#     window.exitonclick()
#
# prozor('mojprozor')

#druga vezba
# import turtle
#
# def prozor(ime,x,y):
#     window = turtle.Screen()
#     window.title(ime)
#     window.setup(x, y)
#     window.exitonclick()
#
# prozor('mojprozor', 200, 400)

# #treca vezba
import turtle

# def prozor(file_path):
#
#     f = open(file_path, "r")
#     config = f.read().split(',')
#     sirina = config[0]
#     visina = config[1]
#     naziv = config[2]
#     window = turtle.Screen()
#     window.setup(int(sirina), int(visina))
#     window.title(naziv)
#     window.exitonclick()
window = create_window_from_file("window_config.txt")
milutin = turtle.RawTurtle(window)
milutin.penup()
milutin.shape('circle')
def move_up():
    x, y = milutin.position()
    milutin.setposition(x, y + 10)
def move_down():
    x, y = milutin.position()
    milutin.setposition(x, y - 10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down(), "Down")
window.listen()


