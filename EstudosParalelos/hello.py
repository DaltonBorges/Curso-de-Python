# -*- coding: utf-8 -*-

import time

import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption('Olá mundo')

screen.fill([30, 90, 80])

pygame.display.flip()

time.sleep(3)