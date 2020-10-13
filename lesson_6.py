from typing import List

import pygame
from pygame.draw import *
from random import randint

pygame.init()

n = 10  # максимальное количество шариков на экране
k = 3  # максимальное количество квадратов на экране
FPS = 30
f = 0
screen = pygame.display.set_mode((1200, 900))
# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# Параметры квадратов
x_rect = [randint(100, 1100) for i2 in range(n)]
y_rect = [randint(100, 900) for i3 in range(n)]
r_rect = [randint(10, 100) for i4 in range(n)]
color_rect = [COLORS[randint(0, 5)] for i5 in range(n)]
# Параметры шариков
v_ball_x = [randint(-10, 10) for j0 in range(n)]
v_ball_y = [randint(-10, 10) for j1 in range(n)]
x_ball = [randint(100, 1100) for j2 in range(n)]
y_ball = [randint(100, 900) for j3 in range(n)]
r_ball = [randint(10, 100) for j4 in range(n)]
color_ball = [COLORS[randint(0, 5)] for j5 in range(n)]
# Счет
score0 = 0
score_ball = 5  # Количество очков за попадание по шарику
score_rect = 12  # Количество очков за попадание по квадрату


def ball_move(x, y, v_x, v_y, r, color):
    """
    Функция реализует смещение шариков в каждый кадр
    :param x: x-координата шарика
    :param y: y-координата шарика
    :param v_x: Увеличение x-координаты шарика в следующий такт
    :param v_y: Увеличение y-координаты шарика в следующий такт
    :param r: Радиус шарика
    :param color: Цвет шарика
    :return: Измененные координаты и скорости шарика (в формате
    x, y, v_x, v_y
    """
    circle(screen, color, (x, y), r)
    x += v_x
    y += v_y
    if (y + v_y >= 900) or (y + v_y <= 0):
        v_y = -v_y
    elif (x + v_x >= 1200) or (x + v_x <= 0):
        v_x = -v_x
    return x, y, v_x, v_y


def old_rect(i):
    """
    Функция реализует отрисовку квадратов на старых местах в каждый
    кадр, если номер кадра не кратен 15(обновление раз в 0,5 секунды)
    :param i: номер квадрата
    :return:
    """
    rect(screen, color_rect[i], (x_rect[i], y_rect[i], r_rect[i], r_rect[i]))


def new_rect(i):
    """
    рисует новый квадрат вместо удаленного в точке со случайными
    координатами и стороной, с одним из цветов из COLORS
    :param i: номер удаленного квадрата
    :return:
    """
    x_rect[i] = randint(100, 1100)
    y_rect[i] = randint(100, 900)
    r_rect[i] = randint(10, 100)
    color_rect[i] = COLORS[randint(0, 5)]
    rect(screen, color_rect[i], (x_rect[i], y_rect[i], r_rect[i], r_rect[i]))


def new_ball(i):
    """
    рисует новый шарик вместо удаленного в точке со случайными
    координатами и радиусом с одним из цветов из COLORS
    :param i: номер удаленного шарика
    :return:
    """
    x_ball[i] = randint(100, 1100)
    y_ball[i] = randint(100, 900)
    r_ball[i] = randint(10, 100)
    color_ball[i] = COLORS[randint(0, 5)]


def click(event, score):
    """
    Функция обрабатывает нажатие на кнопку мыши
    :param event: событие(нажатие на кнопку мыши)
    :param score: текущий счет
    :return: возвращает счет после обработки события
    """
    # Проверка попадания в один из квадратов
    for i in range(k):
        if (event.pos[0] - x_rect[i] <= r_rect[i]) and \
                (event.pos[0] - x_rect[i] >= 0) and \
                (event.pos[1] - y_rect[i] <= r_rect[i]) and \
                (event.pos[1] - y_rect[i] >= 0):
            new_rect(i)
            score += score_rect
            print('Ваш счет', score)
    # Проверка попадания в один из шариков
    for i in range(n):
        if ((event.pos[0] - x_ball[i]) ** 2 +
                (event.pos[1] - y_ball[i]) ** 2 <= r_ball[i] ** 2):
            new_ball(i)
            score += score_ball
            print('Ваш счет', score)
    return score


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    f += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score0 = click(event, score0)
    # отрисовка неудаленных квадратов
    for i in range(k):
        old_rect(i)
    if f % 15 == 0:
        for i in range(k):
            new_rect(i)
    # отрисовка неудаленных шариков
    for i in range(n):
        x_ball[i], y_ball[i], \
        v_ball_x[i], v_ball_y[i] = ball_move(x_ball[i], y_ball[i],
                                             v_ball_x[i], v_ball_y[i],
                                             r_ball[i], color_ball[i])
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
