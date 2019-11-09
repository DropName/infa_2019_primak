from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='old lace')
canv.pack(fill=tk.BOTH, expand=1)

x_t_min = 400  # границы для движения по экрану
x_t_max = 800
y_t_min = 000
y_t_max = 600


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball (пули)
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - радиус мяча
        vx - начальная скорость мяча по горизонтали
        vy - начальня скорость мяча по вертикали
        color - цвет мяча
        id - объект мяча
        live - время жизни
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['burlywood1', 'burlywood2',
                             'burlywood3', 'burlywood4'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        """
        Движение мяча (пули)
        """
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y <= y_t_max + 50:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:

            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 800:
            self.vx = -self.vx / 2
            self.x = 799

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        touched = False
        if abs(obj.x - self.x) <= (self.r + obj.r):
            if abs(obj.y - self.y) <= (self.r + obj.r):
                touched = True
        return touched


class gun():
    """
    Класс пушки, имеет силу зажатия, зависящую от времени зажатия ЛКМ
    balls - пули пушки
    an - угол наклона пушки
    bullet - кол-во пуль
    clr - цвет
    id - обьект пушки
    """

    def __init__(self, bullet, balls, clr):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.bullet = bullet
        self.balls = balls
        self.clr = clr
        self.id = canv.create_line(20, 450, 50, 420, width=7, fill=self.clr)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """
        Прицеливание. Зависит от положения мыши.
        """
        if self.clr == 'DarkOliveGreen3':
            fill = 'DarkOliveGreen3'
        elif self.clr == 'chocolate2':
            fill = 'chocolate2'

        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill=fill)
        else:
            canv.itemconfig(self.id, fill=self.clr)
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """
        Повышение начальной скорости пули из пушки при зажатии ЛКМ
        """
        if self.clr == 'DarkOliveGreen3':
            fill = 'DarkOliveGreen3'
        elif self.clr == 'chocolate2':
            fill = 'chocolate2'
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill=fill)
        else:
            canv.itemconfig(self.id, fill=fill)


class target():
    """
    Класс мишени
    pointsx - очки игрока номер *
    id - объект мишени
    clr - цвет мишени
    """

    def __init__(self, clr):
        self.points1 = 0
        self.points2 = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points1 = canv.create_text(
            30, 30, text='', font='28', fill='DarkOliveGreen3')
        self.id_points2 = canv.create_text(
            30, 60, text='', font='28', fill='chocolate2')
        self.clr = clr
        self.new_target()
        self.vx = choice([-10, 5, 10])
        self.vy = choice([-10, 10])

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = 600
        y = self.y = rnd(250, 550)
        r = self.r = choice([20, 30, 40])
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=self.clr)

    def hit(self, points=1, player=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        if player == 1:
            self.points1 += points
            canv.itemconfig(self.id_points1, text='')
            canv.itemconfig(self.id_points1, text=self.points1)
        elif player == 2:
            self.points2 += points
            canv.itemconfig(self.id_points2, text='')
            canv.itemconfig(self.id_points2, text=self.points2)

    def update(self):
        """
        Движение мишеней
        """
        if self.live:
            self.x += self.vx
            self.y += self.vy
            canv.coords(self.id,
                        self.x - self.r, self.y - self.r,
                        self.x + self.r, self.y + self.r)
            canv.itemconfig(self.id, fill=self.clr)

            if self.x > x_t_max - self.r:
                self.vx *= -1

            if self.y > y_t_max - self.r:
                self.vy *= -1

            if self.x < x_t_min + self.r:
                self.vx *= -1

            if self.y < y_t_min + self.r:
                self.vy *= -1


class game():
    """
    Класс игры
    """

    def __init__(self, bullet, balls, t1, t2, gun1, gun2):
        self.bullet = bullet
        self.balls = balls
        self.screen = canv.create_text(400, 300, text='', font='28')
        self.t1 = t1
        self.t2 = t2
        self.gun1 = gun1
        self.gun2 = gun2
        self.score1 = 0
        self.score2 = 0

    def new_game(self, event=''):
        """
        Один такт игры.
        Такт состоит из хода первого, а затем второго игрока, если не наступило условие победы.
        """
        self.t1.new_target()
        self.t2.new_target()
        canv.bind('<Button-1>', self.gun1.fire2_start)
        canv.bind('<ButtonRelease-1>', self.gun1.fire2_end)
        canv.bind('<Motion>', self.gun1.targetting)

        z = 0.03
        self.t1.live = 1
        self.t2.live = 1
        while self.t1.live and self.t2.live or balls:
            for b in balls:
                b.move()
                if b.hittest(self.t1) and self.t1.live:
                    self.t1.live = 0
                    self.t1.hit(points=11 - self.gun1.bullet, player=1)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(
                        self.screen, text='Вы получаете: ' + str(11 - self.gun1.bullet))
                    self.score1 += 11 - self.gun1.bullet
                    self.gun1.bullet = 0

                elif b.hittest(self.t2) and self.t2.live:
                    self.t2.live = 0
                    self.t2.hit(points=self.gun1.bullet, player=2)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(
                        self.screen, text='Ваш враг получает: ' + str(self.gun1.bullet))
                    self.score2 += self.gun1.bullet
                    self.gun1.bullet = 0

            canv.update()
            time.sleep(z)
            self.gun1.targetting()
            self.gun1.power_up()
            t1.update()
            t2.update()

        canv.itemconfig(self.screen, text='')
        canv.delete(self.gun1)
        if self.score1 > 100:
            canv.itemconfig(self.screen, text='Побеждает Оливковый игрок')
        elif self.score2 > 100:
            canv.itemconfig(self.screen, text='Побеждает Шоколадный игрок')

        self.t1.new_target()
        self.t2.new_target()
        canv.bind('<Button-1>', self.gun2.fire2_start)
        canv.bind('<ButtonRelease-1>', self.gun2.fire2_end)
        canv.bind('<Motion>', self.gun2.targetting)

        z = 0.03
        self.t1.live = 1
        self.t2.live = 1
        while self.t1.live and self.t2.live or balls:
            for b in balls:
                b.move()
                if b.hittest(self.t1) and self.t1.live:
                    self.t1.live = 0
                    self.t1.hit(points=self.gun2.bullet, player=1)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')

                    canv.itemconfig(
                        self.screen, text='Ваш враг получает: ' + str(self.gun2.bullet))
                    self.score1 += self.gun2.bullet
                    self.gun2.bullet = 0

                elif b.hittest(self.t2) and self.t2.live:
                    self.t2.live = 0
                    self.t2.hit(points=11 - self.gun2.bullet, player=2)
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(
                        self.screen, text='Вы получаете: ' + str(11 - self.gun2.bullet))
                    self.score2 += 11 - self.gun2.bullet
                    self.gun2.bullet = 0

            canv.update()
            time.sleep(z)
            self.gun2.targetting()
            self.gun2.power_up()
            t1.update()
            t2.update()

        canv.itemconfig(self.screen, text='')
        canv.delete(self.gun2)

        if self.score1 > 100:
            canv.itemconfig(self.screen, text='Побеждает Оливковый игрок')
        elif self.score2 > 100:
            canv.itemconfig(self.screen, text='Побеждает Шоколадный игрок')

        root.after(750, game.new_game)


bullet = 0
balls = []
t1 = target(clr='DarkOliveGreen3')
t2 = target(clr='chocolate2')
g1 = gun(bullet=0, balls=balls, clr='DarkOliveGreen3')
g2 = gun(bullet=0, balls=balls, clr='chocolate2')
game = game(balls=balls, bullet=bullet, gun1=g1, gun2=g2, t1=t1, t2=t2)

game.new_game()

tk.mainloop()
