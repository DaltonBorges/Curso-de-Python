import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 640
altura = 480
x = largura / 2 -20
y = altura /2 - 25
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(32)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            elif event.key == K_d:
                x += 20
            elif event.key == K_w:
                y -= 20
            elif event.key == K_s:
                y += 20
        '''
        if pygame.key.get_pressed()[K_a]:
            x -= 20
        elif pygame.key.get_pressed()[K_d]:
            x += 20
        elif pygame.key.get_pressed()[K_w]:
            y -= 20
        elif pygame.key.get_pressed()[K_s]:
            y += 20

        pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
        pygame.display.update()
