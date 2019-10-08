#!/usr/bin/env python

background_image_file = 'image/sushiplate.jpg'
mouse_image_file = 'image/fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
 
screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_file).convert()
mouse_cursor = pygame.image.load(mouse_image_file).convert_alpha()

def mouseMoveCursor():
    Fullscreen = False
    move_x, move_y = 0, 0
    before_cursor_x , before_cursor_y = 0, 0
    before_x, before_y = 0, 0
    while True:
        hasKeyMove = False
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    Fullscreen = not Fullscreen
                    global screen
                    if Fullscreen:
                        screen = pygame.display.set_mode((640, 480),
                                                         FULLSCREEN, 32)
                    else:
                        screen = pygame.display.set_mode((640,480), 0, 32)
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -1
                elif event.key == K_RIGHT:
                    move_x = 1
                elif event.key == K_UP:
                    move_y = -1
                elif event.key == K_DOWN:
                    move_y = 1
            elif event.type == KEYUP:
                move_x = 0
                move_y = 0
           

        screen.blit(background, (0, 0))

        if move_x == 0 and move_y ==0:
            x, y = pygame.mouse.get_pos()
            if x == before_cursor_x and y == before_cursor_y:
                before_cursor_x, before_cursor_y = x, y
                if hasKeyMove:
                    x, y = before_x, before_y
            else:
                before_cursor_x, before_cursor_y = x, y
                hasKeyMove = False
            x -= mouse_cursor.get_width() / 2
            y -= mouse_cursor.get_height() / 2
        else:
            x,y = before_x, before_y
            x += move_x
            y += move_y
            hasKeyMove = True

        before_x , before_y = x, y
        screen.blit(mouse_cursor, (x, y))
        
        pygame.display.update()

def keyboardMoveCursor():
    key_x , key_y = 0, 0
    move_x, move_y = 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -1
                elif event.key == K_RIGHT:
                    move_x = 1
                elif event.key == K_UP:
                    move_y = -1
                elif event.key == K_DOWN:
                    move_y = 1
            elif event.type == KEYUP:
                move_x = 0
                move_y = 0

        key_x += move_x
        key_y += move_y
        screen.blit(background, (0, 0))
        screen.blit(mouse_cursor, (key_x, key_y))
        pygame.display.update()

def resizeWindow():
    SCREEN_SIZE = (640, 480)
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            exit()
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            
        screen_width, screen_height = SCREEN_SIZE

        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x, y))

        pygame.display.update()

#resizeWindow()
#keyboardMoveCursor()
mouseMoveCursor()

