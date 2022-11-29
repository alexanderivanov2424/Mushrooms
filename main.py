import pygame
from pygame.locals import *

import numpy as np
import time
import os

from mushroom import Mushroom


window_size = (600, 600)

pygame.init()
screen = pygame.display.set_mode(window_size, RESIZABLE)
pygame.display.set_caption("Mushrooms")

mushroom = Mushroom()

background1 = pygame.image.load("background1.jpg")
background2 = pygame.image.load("background2.jpg")
background3 = pygame.image.load("background3.jpg")
background = np.random.choice([background1, background2, background3]).convert_alpha()

def render():
    screen.fill((255, 255, 255))

    scale = 1
    mushroom_generation_size = 600 # This shouldn't change
    mushroom_screen = pygame.Surface((mushroom_generation_size, mushroom_generation_size))

    mushroom_screen.blit(background, (mushroom_generation_size/2 - background.get_size()[0]/2, mushroom_generation_size - background.get_size()[1]))

    mushroom.draw(mushroom_screen)
    mushroom_screen = pygame.transform.scale(mushroom_screen, (mushroom_generation_size * scale, mushroom_generation_size * scale))

    w, h = screen.get_size()
    screen.blit(mushroom_screen, (w/2 - scale * mushroom_generation_size / 2, h - mushroom_generation_size * scale))

    pygame.display.update()

while True:
    render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_n:
                mushroom = Mushroom()
            if event.key == pygame.K_b:
                mushroom.generate_colors()
        if pygame.mouse.get_pressed()[0]:
            mushroom = Mushroom()
