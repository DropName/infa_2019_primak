from graph import brushColor, penColor, penSize
from graph import circle, line, polygon, point, rectangle
from graph import canvasSize, windowSize, run

from random import randint
import math as m


def apple(x, y, size, mirror):
    """
    apple function draws the apple of the radius r pxls for size = 1
        there are 3 components:
                1) main body
                2) root, represented by a line
                3) leaf, which is obviously a sqrt curve

            The coords of root and leaf are given regarding to r of an main body,
            so all "strange" numbers in the further functions are also just a calibrate number for beauty's purposes
            (._.)

            mirror is for drawing mirrored images
    """
    # apple body
    penColor(245, 84, 84)
    penSize(0)
    brushColor(245, 84, 84)
    circle(x, y, 25 * size)
    # root
    penColor("black")
    penSize(2 * size)
    line(x, y - size * 20, x + size * 12.5 * mirror, y - size * 42.5)
    # leaf
    brushColor(100, 225, 100)
    penSize(size)
    polygon(curve(x + size * 2.5 * mirror, y - size * 27.5, size, mirror))


def curve(x, y, size, mirror):
    """
    function, wich draws polygon sqrt-shape like
    """
    res = []
    for i in range(25):
        res.append((x + mirror * i * 1.5 * size, y - (7 * size) * (i**0.3)))
    return res


def ufo(x, y, size):
    """
    ufo function creates an ufo, which consists of 3 types of objests:
            1) ufo_light is the light underneath the space ship
            2) ufo_ship is the ship itself
            3) ufo_lamp is lamp, plased on the ship, it is possible to change their coords,
            change their size and rotation
            🛸
    """
    ufo_light(x, y, size)

    ufo_ship(x, y, size)

    ufo_lamp(x, y + 3 * size, size)
    ufo_lamp(x - 8 * size, y + 2 * size, size)
    ufo_lamp(x + 8 * size, y + 2 * size, size)
    ufo_lamp(x - 14 * size, y + 0.05 * size, size)
    ufo_lamp(x + 14 * size, y + 0.05 * size, size)


def ufo_light(x, y, size):
    # light - light pillar of an ufo
    penSize(0)
    brushColor(210, 250, 210)
    penColor(210, 250, 210)
    light = []
    light.append((x, y))
    light.append((x - 20 * size, y + 20 * size))
    light.append((x + 20 * size, y + 20 * size))
    polygon(light)


def ufo_ship(x, y, size):
    # main body
    brushColor(168, 168, 168)
    penColor(168, 168, 168)
    ellips(x, y, 20 * size, 5 * size, 0)
    # glass
    brushColor(180, 220, 220)
    penColor(180, 220, 220)
    ellips(x, y - 3 * size, 12 * size, 4 * size, 0)


def ufo_lamp(x, y, size, rotate=0):
    # lamps
    brushColor('white')
    penColor('white')
    ellips(x, y, 3 * size, 1 * size, 0)


def ellips(x, y, a, b, f):
    """
    a - x radius; b - y radius; f - angle(dgr)

    """
    f = f * m.pi / 180
    x_e = [i for i in range(-a, a)]
    y1, y2 = [], []
    for i in range(len(x_e)):
        xy1 = [x_e[i], b * (1 - (x_e[i] / a)**2)**0.5]
        xy2 = [x_e[i], -b * (1 - (x_e[i] / a)**2)**0.5]
        xy1 = [xy1[0] * m.cos(f) - xy1[1] * m.sin(f), xy1[0]
               * m.sin(f) + xy1[1] * m.cos(f)]
        xy2 = [xy2[0] * m.cos(f) - xy2[1] * m.sin(f), xy2[0]
               * m.sin(f) + xy2[1] * m.cos(f)]
        y1.append((xy1[0] + x, xy1[1] + y))
        y2.append((xy2[0] + x, xy2[1] + y))
    y2 = y2[::-1]
    polygon(y1 + y2)


def alien(x, y, size, mirror, color='#C7F971'):
    """
    alien has a lot of atributes (it is possible to constract one by yourself):
            1)body consists of the main_body and ass (ass is able to be rotated)
            2)there are to types of hands: up and down
            3)two types of legs
            4)head part includes the head itself, horns, eyes
            5)apple (which is not necessary, but according to the task it is much easier to place apple function here)

            also it is possible to change proportions of an any part of the alien in the code section,
            by the way this alien is easy to be painted in any color

            p.s. alein's balls can be painted differentely by adding color atribute to the horns function
            (.Y.)
    """
    penColor(color)
    brushColor(color)

    main_body(x, y, size)
    ass(x, y, size)

    hand_down(x, y, size, mirror)
    hand_up(x, y, size, mirror)

    leg_left(x, y, size, mirror)
    leg_right(x, y, size, mirror)

    head(x, y, size)
    eyes(x, y, size, mirror)
    horns(x, y, size, "blue")

    apple(x + 3 * size * mirror, y - size * 3.2, size / 28, mirror)


def alien_simple(x, y, size, mirror, color='#C7F971'):
    """
    just another type of an alien
    """
    penColor(color)
    brushColor(color)

    main_body(x, y, size)
    ass(x, y, size)

    hand_down(x, y, size, mirror)
    hand_up(x, y, size, mirror)

    leg_left(x, y, size, mirror)
    leg_right(x, y, size, mirror)

    head(x, y, size)
    eyes(x, y, size, mirror)
    horns(x, y, size)


def alien_handy(x, y, size, mirror, color='#C7F971'):
    """
    just another type of an alien
    """
    penColor(color)
    brushColor(color)

    main_body(x, y, size)
    ass(x, y, size)

    hand_down(x, y, size, mirror)
    hand_down(x, y, size, -mirror)
    hand_up(x, y, size, -mirror)
    hand_up(x, y, size, mirror)

    leg_left(x, y, size, mirror)
    leg_right(x, y, size, mirror)

    head(x, y, size)
    eyes(x, y, size, mirror)
    horns(x, y, size)


def main_body(x, y, size, rotate=0):
    # main body
    ellips(x, y, size, 1.5 * size // 1, 0)
    # neck
    rectangle(x - 0.15 * size, y + 1 * size - 3 * size,
              x + 0.15 * size, y + 3 * size - 3 * size)


def hand_down(x, y, size, mirror):
    """
    standart: stands for the left hand
    """
    ellips(x - 1.1 * size * mirror, y - 0.7 * size, size // 2, size // 3, 0)
    ellips(x - 1.5 * size * mirror, y - 0.2 *
           size, size // 2, size * 1.2 // 2, 30 * mirror)
    ellips(x - 2.5 * size * mirror, y + 0.5 * size,
           size // 2, size * 0.8 // 1, -100 * mirror)


def hand_up(x, y, size, mirror):
    """
    standart: stands for the right hand
    """
    ellips(x + 1.1 * size * mirror, y - 1.2 * size, size // 2, size // 3, 0)
    ellips(x + 2.1 * size * mirror, y - 1.4 *
           size, int(size / 1.1), int(size // 2.5), -20 * mirror)
    ellips(x + 2.5 * size * mirror, y - 2.1 * size,
           int(size / 1.6), int(size / 2.4), 10 * mirror)


def ass(x, y, size, rotate=0):
    ellips(x, y + size * 1.5, size, size, rotate)


def leg_left(x, y, size, mirror):
    ellips(x + size * mirror, y + size * 2.7,
           size // 2, size // 1, -10 * mirror)
    ellips(x + size * mirror, y + size * 4, size // 2, size // 1, -10 * mirror)
    ellips(x + 1.6 * size * mirror, y + size * 5,
           size // 2, size * 0.9 // 1, -90 * mirror)


def leg_right(x, y, size, mirror):
    ellips(x - size * mirror, y + size * 2.7, size //
           2, size // 1, 10 * mirror)
    ellips(x - 1.3 * size * mirror, y + size *
           4, size // 2, size // 1, 10 * mirror)
    ellips(x - 1.8 * size * mirror, y + size * 5,
           size // 2, size * 0.9 // 1, 70 * mirror)


def head(x, y, size):
    penSize(size // 2)
    polygon([(x + 1.6 * size, y - 3 * size),
             (x, y + 1 * size - 3 * size), (x - 1.6 * size, y - 3 * size)])


def horns(x, y, size, color="red"):
    """
    note: it is possible to change the cf alien's ball (horn balls)
    """
    penSize(0.5 * size)
    line(x + 1.6 * size, y - 3 * size, x + 2.2 * size, y - 4 * size)
    line(x - 1.6 * size, y - 3 * size, x - 2.2 * size, y - 4 * size)

    brushColor(color)
    penSize(0.15 * size)
    circle(x + 2.3 * size, y - 4.1 * size, 0.3 * size)
    circle(x - 2.3 * size, y - 4.1 * size, 0.3 * size)


def eyes(x, y, size, mirror):
    """
    draws two black circles and two ellipses inside them, the coord of middle point is (x,y), can be mirrored
    """
    penSize(1)
    brushColor('black')
    circle(x + 1 * size, y - 2.8 * size, size // 2)
    circle(x - 1 * size, y - 2.8 * size, size // 2)
    brushColor('white')
    ellips(x + 1.2 * size * mirror, y - 2.9 * size, size // 6, size // 4, 0)
    ellips(x - 0.8 * size * mirror, y - 2.9 * size, size // 6, size // 4, 0)


def cloud(x, y, size, color):
    """
    just 3 elipses along each other
    """
    colinc = 10
    brushColor(color + colinc, color + colinc, color + colinc)
    penColor(color + colinc, color + colinc, color + colinc)
    ellips(x - 1.2 * size, y, size, size, 0)
    ellips(x, y, size, size, 0)
    ellips(x + 1.2 * size, y, size, size, 0)


def star(x_star, y_star):
    """
    draws a star '+' shaped
    """
    penColor(255, 244, 164)
    point(x_star, y_star)
    point(x_star + 1, y_star)
    point(x_star - 1, y_star)
    point(x_star, y_star + 1)
    point(x_star, y_star - 1)


def starry_sky(n, width=500, height=400):
    """
    randomly splits n stars across the rectangle with height and width
    """
    for i in range(n):
        star(randint(0, width), randint(0, height))


def fancy_cloud(x, y, size, n):
    """
    draws n clouds with decreasing size, creates gradient effect
    """
    for i in range(n):
        cloud(x, y, size - i // 2, i)


windowSize(600, 800)
canvasSize(500, 800)

brushColor(70, 50, 90)
rectangle(0, 0, 500, 400)

brushColor(59, 135, 59)
rectangle(0, 400, 500, 800)

brushColor(255, 244, 164)
circle(350, 120, 100)

starry_sky(200)

fancy_cloud(350, 180, 70, 100)
fancy_cloud(400, 40, 50, 100)
fancy_cloud(180, 30, 60, 70)

ufo(440, 100, 3)
ufo(50, 300, 5)
ufo(280, 280, 7)

alien(60, 360, 15, -1, "yellow")
alien(330, 420, 20, 1)
alien_handy(460, 370, 14, -1, "orange")
alien_simple(240, 470, 13, 1, "purple")


run()
