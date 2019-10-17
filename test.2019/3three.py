import math as m


def rotate_square(coords, angle):
    """
    rotates a square with coords (star) by angle(dgr, clockwise) 
    """
    x0 = (coords[0][0] + coords[1][0] + coords[2][0] + coords[3][0]) / 4
    y0 = (coords[0][1] + coords[1][1] + coords[2][1] + coords[3][1]) / 4
    a = angle * m.pi / 180
    rotation = []
    for i in range(4):
        x = coords[i][0] - x0
        y = coords[i][1] - y0
        x_pnt = x * m.cos(a) + x * m.sin(a)
        y_pnt = y * m.cos(a) - y * m.sin(a)
        rotation.append((round(x_pnt + x0, ), y_pnt + y0))
    return rotation


print(rotate_square([(0, 0), (1, 0), (1, 1), (0, 1)], 90))
