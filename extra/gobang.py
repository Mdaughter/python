#coding:utf-8
import pygame
import time
from pygame.locals import *

white = (255, 255, 255)
blue = (0, 0, 200)
black = (0, 0, 0)
green = (0, 155, 0)
brightblue = (0, 50, 255)
yellow = (255, 255, 0)
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("五子棋")
myfont = pygame.font.SysFont("arial", 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
    background = pygame.image.load('gomokubackground.png')
    screen.blit(background, (0, 0))
    i1 = 0
    while i1 < 401:
        pygame.draw.line(screen, yellow, (i1, 0), (i1, 400), 1)
        i1 = i1 + 20
    i2 = 0
    while i2 < 401:
        pygame.draw.line(screen, yellow, (0, i2), (400, i2), 1)
        i2 = i2 + 20
    pygame.display.update()
    list1 = []
    list2 = []
    list3 = []
    change = 0
    g = 0
    m = 0
    n = 0
    while g == 0:
        if change % 2 == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    a, b = event.pos
                    if not ((round(a / 20), round(b / 20)) in list3):
                        a1 = round(a / 20)
                        b1 = round(b / 20)
                        list1.append((a1, b1))
                        list3.append((a1, b1))
                        pygame.draw.circle(screen, white, (20 * a1, 20 * b1), 8, 0)
                        pygame.display.update()
                        for m in range(21):
                            for n in range(21):
                                if n < 17 and (m, n) in list1 and (m, n + 1) in list1 and (m, n + 2) in list1 and (
                                        m, n + 3) in list1 and (m, n + 4) in list1:
                                    g = 1
                                elif m < 17 and (m, n) in list1 and (m + 1, n) in list1 and (m + 2, n) in list1 and (
                                        m + 3, n) in list1 and (m + 4, n) in list1:
                                    g = 1
                                elif m < 17 and n < 17 and (m, n) in list1 and (m + 1, n + 1) in list1 and (
                                        m + 2, n + 2) in list1 and (m + 3, n + 3) in list1 and (m + 4, n + 4) in list1:
                                    g = 1
                                elif m < 17 and n > 3 and (m, n) in list1 and (m + 1, n - 1) in list1 and (
                                        m + 2, n - 2) in list1 and (m + 3, n - 3) in list1 and (m + 4, n - 4) in list1:
                                    g = 1
                                else:
                                    change = change + 1
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    a, b = event.pos
                    if not ((round(a / 20), round(b / 20)) in list3):
                        a2 = round(a / 20)
                        b2 = round(b / 20)
                        list2.append((a2, b2))
                        list3.append((a2, b2))
                        pygame.draw.circle(screen, black, (20 * a2, 20 * b2), 8, 0)
                        pygame.display.update()
                        for m in range(21):
                            for n in range(21):
                                if n < 17 and (m, n) in list2 and (m, n + 1) in list2 and (m, n + 2) in list2 and (
                                        m, n + 3) in list2 and (m, n + 4) in list2:
                                    g = 2
                                elif m < 17 and (m, n) in list2 and (m + 1, n) in list2 and (m + 2, n) in list2 and (
                                        m + 3, n) in list2 and (m + 4, n) in list2:
                                    g = 2
                                elif m < 17 and n < 17 and (m, n) in list2 and (m + 1, n + 1) in list2 and (
                                        m + 2, n + 2) in list2 and (m + 3, n + 3) in list2 and (m + 4, n + 4) in list2:
                                    g = 2
                                elif m < 17 and n > 3 and (m, n) in list2 and (m + 1, n - 1) in list2 and (
                                        m + 2, n - 2) in list2 and (m + 3, n - 3) in list2 and (m + 4, n - 4) in list2:
                                    g = 2
                                else:
                                    change = change + 1
    if g == 1:
        message = myfont.render("WRITE", True, green)
        screen.blit(message, (100, 100))
    if g == 2:
        message = myfont.render("BLACK", True, green)
        screen.blit(message, (100, 100))
    message = myfont.render("GAMEOVER", True, green)
    screen.blit(message, (50, 50))
    pygame.display.update()
    pygame.time.wait(3000)