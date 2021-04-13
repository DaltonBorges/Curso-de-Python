import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.3)
bg_m = pygame.mixer.music.load('box_cat.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.9)

largura = 640
altura = 480

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 22, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu Jogo')
relogio = pygame.time.Clock()
lista_corpo = []
comprimento_inicial = 5

def aumenta_cobra(lista_corpo):
    for XeY in lista_corpo:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

while True:
    relogio.tick(30)
    tela.fill((0, 50, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 0, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            elif event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            elif event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0
            elif event.key == K_s:
                if y_controle == - velocidade:
                    pass
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += x_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_corpo.append(lista_cabeca)

    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]

    aumenta_cobra(lista_corpo)

    tela.blit(texto_formatado, (10, 10))
    pygame.display.update()
