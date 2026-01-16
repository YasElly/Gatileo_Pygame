import pygame

pygame.init()
pygame.display.set_caption('Gatíleo')
largura = 640
altura = 480
font = pygame.font.Font(None, 24)
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
running = True

titulo = pygame.image.load('gatileo/imagens/titulo2.png').convert_alpha()
titulo = pygame.transform.smoothscale(titulo, (300, 96))

tela_inicial = pygame.image.load('gatileo/imagens/img1.png')
tela_inicial = tela_inicial.convert()  