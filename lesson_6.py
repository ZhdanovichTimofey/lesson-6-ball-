from typing import List

import pygame
from pygame.draw import *
from random import randint

pygame.init()

n = 10  # максимальное количество шариков на экране
k = 3  # максимальное количество квадратов на экране
FPS = 30
t = 20  # Время игры
f = 0
# Таблица рекордов
names = ['0' for y in range(10)]
records = [0 for i in range(10)]
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
# Счет
score0 = 0


def read_records():
    """
    Функция заносит в память программы таблицу рекордов
    :return:
    """
    input1 = open('record table sys.txt', 'r')
    input2 = open('record table sys 1.txt', 'r')
    r = input1.readlines()
    names_local = input2.readlines()
    for i in range(10):
        names[i] = names_local[i].rstrip()
        r[i] = r[i].rstrip()
        records[i] = int(r[i])
    input1.close()
    input2.close()

class Ball(object):
    def __init__(self):
        """
        Создание нового объекта из класса шариков
        """
        self.score = 5
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)

    def ball_move(self):
        """
        Функция реализует смещение шариков в каждый кадр
        :return:
        """
        circle(screen, self.color, (self.x, self.y), self.r)
        self.x += self.vx
        self.y += self.vy
        if (self.y + self.vy >= 900) or (self.y + self.vy <= 0):
            self.vy = -self.vy
        elif (self.x + self.vx >= 1200) or (self.x + self.vx <= 0):
            self.vx = -self.vx

    def new_ball(self):
        """
        рисует новый шарик вместо удаленного в точке со случайными
        координатами и радиусом с одним из цветов из COLORS
        :return:
        """
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)

    def ball_click(self, event, score):
        """
        Функция проверяет попадание по шарику
        :param event: событие(нажатие на кнопку мыши)
        :param score: текущий счет
        :return: возвращает счет после обработки события
        """
        if ((event.pos[0] - self.x) ** 2 +
                (event.pos[1] - self.y) ** 2 <= self.r ** 2):
            self.new_ball()
            score += self.score
            print('Ваш счет', score)
        return score


class Rect(object):
    """
    Класс квадратов
    """
    def __init__(self):
        """
        Создание нового объекта из класса квадратов
        """
        self.score = 12
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        rect(screen, self.color,
             (self.x, self.y, self.r, self.r))

    def old_rect(self):
        """
        Функция реализует отрисовку квадратов на старых местах в каждый
        кадр, если номер кадра не кратен 15(обновление раз в 0,5 секунды)
        :return:
        """
        rect(screen, self.color,
             (self.x, self.y, self.r, self. r))

    def new_rect(self):
        """
        рисует новый квадрат вместо удаленного в точке со случайными
        координатами и стороной, с одним из цветов из COLORS
        :return:
        """
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        rect(screen, self.color,
             (self.x, self.y, self.r, self.r))

    def rect_click(self, event, score):
        """
        Функция проверяет попадание по квадрату
        :param event: событие(нажатие на кнопку мыши)
        :param score: текущий счет
        :return: возвращает счет после обработки события
        """
        if (event.pos[0] - self.x <= self.r) and \
                (event.pos[0] - self.x) and \
                (event.pos[1] - self.y <= self.r) and \
                (event.pos[1] - self.y >= 0):
            self.new_rect()
            score += self.score
            print('Ваш счет', score)
        return score


def click(event, score):
    """
    Функция обрабатывает нажатие на кнопку мыши
    :param event: событие(нажатие на кнопку мыши)
    :param score: текущий счет
    :return: возвращает счет после обработки события
    """
    # Проверка попадания в один из квадратов
    for i in range(k):
        score = rectangle[i].rect_click(event, score)
    # Проверка попадания в один из шариков
    for i in range(n):
        score = ball[i].ball_click(event, score)
    return score


def end_game():
    """
    Функция записывает результат игры в таблицу рекордов и завершает
    игру
    :return: finished = True. Завершает игру
    """
    finish = True
    output1 = open('record table.txt', 'w')
    output2 = open('record table sys.txt', 'w')
    output3 = open('record table sys 1.txt', 'w')
    i = 0
    while i < 10:
        if records[i] < score0:
            for j in range(8, i, -1):
                names[j + 1] = names[j]
                records[j + 1] = records[j]
            names[i] = input()
            records[i] = score0
            i = 10
        i += 1
    for i in range(10):
        print(names[i], ': ', records[i], file=output1)
        print(records[i], file=output2)
        print(names[i], file=output3)
    return finish


pygame.display.update()
clock = pygame.time.Clock()
finished = False
# Заносим таблицу рекордов
read_records()
# Cоздаем шарики
ball = [Ball() for j in range(n)]
# Создаем квадраты
rectangle = [Rect() for k in range(k)]
while not finished:
    clock.tick(FPS)
    f += 1
    # Конец игры
    if f == t * FPS:
        finished = end_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score0 = click(event, score0)
    # отрисовка неудаленных квадратов
    for i in range(k):
        rectangle[i].old_rect()
    if f % 15 == 0:
        for i in range(k):
            rectangle[i].new_rect()
    # отрисовка неудаленных шариков
    for i in range(n):
        ball[i].ball_move()
    pygame.display.update()
    pygame.display.set_caption(str(score0))
    screen.fill(BLACK)

pygame.quit()
