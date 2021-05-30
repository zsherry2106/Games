#!/usr/bin/python3

import pygame
from pygame.locals import *
import sys, os
import time

pygame.init()

mouse = pygame.mouse
fpsClock = pygame.time.Clock()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
canvas = window.copy()

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

RED = pygame.Color(242, 44, 44)
ORANGE = pygame.Color(255, 188, 85)
YELLOW = pygame.Color(255, 255, 85)
GREEN = pygame.Color(85, 255, 108)
BLUE = pygame.Color(85, 165, 255)
PURPLE = pygame.Color(216, 85, 255)

L_RED = pygame.Color(243, 111, 111)
L_ORANGE = pygame.Color(255, 206, 131)
L_YELLOW = pygame.Color(250, 250, 195)
L_GREEN = pygame.Color(167, 255, 179)
L_BLUE = pygame.Color(144, 196, 255)
L_PURPLE = pygame.Color(236, 169, 255)
L_BLACK = pygame.Color(82, 82, 82)

GRAY = pygame.Color(206, 206, 206)

ERASER = pygame.image.load("images/ERASER.png")
CLEAR = pygame.image.load("images/clear.png")

def button(x, y, w, h, ic, ac):
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        return pygame.draw.rect(canvas, ac, (x, y, w, h))
    else:
        return pygame.draw.rect(canvas, ic, (x, y, w, h))
        
def stamp(x, y, r, ic, ac):
    if x+r > mouse[0] > x-r and y+r > mouse[1] > y-r:
        return pygame.draw.circle(canvas, ac, (x, y), r)
    else:
        return pygame.draw.circle(canvas, ic, (x, y), r)

def trans(x, y, w, h, ac):
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        s = pygame.Surface((30, 30))
        s.set_alpha(5)
        s.fill((ac))
        canvas.blit(s, (x, y))
    else:
        canvas.blit(ERASER, (735, 540))

    eraser_rect = ERASER.get_rect()
    eraser_rect.x = x
    eraser_rect.y = y
    return eraser_rect

def size(x, y, r, b, ic, ac):
    if x+b > mouse[0] > x-b and y+b > mouse[1] > y-b:
        return pygame.draw.circle(canvas, ac, (x, y), r)
    else:
        return pygame.draw.circle(canvas, ic, (x, y), r)

def color(x, y, w, h, ic, ac):
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        return pygame.draw.rect(canvas, ac, (x, y, w, h))
    else:
        return pygame.draw.rect(canvas, ic, (x, y, w, h))

mouse_color = BLACK
r_size = 5
m_shape = "circle"
background = WHITE
alter = WHITE
m_shape = "round"
canvas.fill(background)
canvas.blit(ERASER, (735, 540))
while True:
    left_pressed, middle_pressed, right_pressed = pygame.mouse.get_pressed()

    mouse = pygame.mouse.get_pos()

    R_Color = button(45, 540, 30, 30, RED, L_RED)
    O_Color = button(135, 540, 30, 30, ORANGE, L_ORANGE)
    Y_Color = button(235, 540, 30, 30, YELLOW, L_YELLOW)
    G_Color = button(335, 540, 30, 30, GREEN, L_GREEN)
    B_Color = button(435, 540, 30, 30, BLUE, L_BLUE)
    P_Color = button(535, 540, 30, 30, PURPLE, L_PURPLE)
    Bl_Color = button(635, 540, 30, 30, BLACK, L_BLACK)
    W_Color = trans(735, 540, 30, 30, WHITE)

    Square_Shape = button(675, 15, 30, 30, BLACK, L_BLACK)
    Circle_Shape = stamp(620, 30, 15, BLACK, L_BLACK)

    Small_Size = size(45, 20, 5, 30, BLACK, GRAY)
    Medium_Size = size(95, 20, 10, 30, BLACK, GRAY)
    Large_Size = size(145, 20, 15, 30, BLACK, GRAY)

    R_Background = color(45, 500, 30, 30, L_RED, RED)
    O_Background = color(135, 500, 30, 30, L_ORANGE, ORANGE)
    Y_Background = color(235, 500, 30, 30, L_YELLOW, YELLOW)
    G_Background = color(335, 500, 30, 30, L_GREEN, GREEN)
    B_Background = color(435, 500, 30, 30, L_BLUE, BLUE)
    P_Background = color(535, 500, 30, 30, L_PURPLE, PURPLE)
    Bl_Background = color(635, 500, 30, 30, L_BLACK, BLACK)
    W_Background = color(735, 500, 30, 30, WHITE, GRAY)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if left_pressed:
            mouse = pygame.mouse.get_pos()
            if R_Color.collidepoint(mouse):
                mouse_color = RED 
            elif O_Color.collidepoint(mouse):
                mouse_color = ORANGE
            elif Y_Color.collidepoint(mouse):
                mouse_color = YELLOW
            elif G_Color.collidepoint(mouse):
                mouse_color = GREEN
            elif B_Color.collidepoint(mouse):
                mouse_color = BLUE
            elif P_Color.collidepoint(mouse):
                mouse_color = PURPLE
            elif Bl_Color.collidepoint(mouse):
                mouse_color = BLACK
            elif W_Color.collidepoint(mouse):
                mouse_color = WHITE

            elif Small_Size.collidepoint(mouse):
                r_size = 5
            elif Medium_Size.collidepoint(mouse):
                r_size = 10
            elif Large_Size.collidepoint(mouse):
                r_size = 15

            if m_shape == "square":
                pygame.draw.rect(canvas, mouse_color, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10))
            if m_shape == "circle":
                pygame.draw.circle(canvas, mouse_color, (pygame.mouse.get_pos()), r_size)


    window.fill(background)
    window.blit(canvas, (0, 0))
    if m_shape == "square":
        pygame.draw.rect(window, mouse_color, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10))
    if m_shape == "circle":
        pygame.draw.circle(window, mouse_color, (pygame.mouse.get_pos()), r_size)
    
    if left_pressed:
        if R_Background.collidepoint(mouse):
            canvas.fill(L_RED)
            background = L_RED
        elif O_Background.collidepoint(mouse):
            canvas.fill(L_ORANGE)
            background = L_ORANGE
        elif Y_Background.collidepoint(mouse):
            canvas.fill(L_YELLOW)
            background = L_YELLOW
        elif G_Background.collidepoint(mouse):
            canvas.fill(L_GREEN)
            background = L_GREEN
        elif B_Background.collidepoint(mouse):
            canvas.fill(L_BLUE)
            background = L_BLUE
        elif P_Background.collidepoint(mouse):
            canvas.fill(L_PURPLE)
            background = L_PURPLE
        elif Bl_Background.collidepoint(mouse):
            canvas.fill(L_BLACK)
            background = L_BLACK
        elif W_Background.collidepoint(mouse):
            canvas.fill(WHITE)
            background = WHITE

        elif clear_rect.collidepoint(mouse):
            window.fill(background)
            canvas.fill(background)

        elif Square_Shape.collidepoint(mouse):
            m_shape = "square"
        elif Circle_Shape.collidepoint(mouse):
            m_shape = "circle"

    clear_rect = pygame.draw.rect(canvas, background, (735, 15, 35, 34))
    canvas.blit(CLEAR, (735, 15))

    pygame.display.flip()
    #fpsClock.tick(1000)
