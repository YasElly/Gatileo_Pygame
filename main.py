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

tela_loja = pygame.image.load("gatileo/imagens/imgloja.png")
tela_loja = tela_loja.convert()

tutorial1 = pygame.image.load('gatileo/imagens/tutorial1.png')
tutorial1 = tutorial1.convert()
tutorial2 = pygame.image.load('gatileo/imagens/tutorial2.png')
tutorial2 = tutorial2.convert()
tutorial_loja = pygame.image.load('gatileo/imagens/tutorial_loja.png')
tutorial_loja = tutorial_loja.convert()

tela_comprou_granada = pygame.image.load("gatileo/imagens/comprou_granada.png")
tela_comprou_granada = tela_comprou_granada.convert()

tela_granada_inventario = pygame.image.load("gatileo/imagens/granada_inventario.png")
tela_granada_inventario = tela_granada_inventario.convert()

tela_comprou_viratempo = pygame.image.load("gatileo/imagens/comprou_viratempo.png")
tela_comprou_viratempo = tela_comprou_viratempo.convert()

tela_viratempo_inventario = pygame.image.load("gatileo/imagens/viratempo_inventario.png")
tela_viratempo_inventario = tela_viratempo_inventario.convert()

tela_dinheiro_insuficiente = pygame.image.load("gatileo/imagens/dinheiro_insuficiente.png")
tela_dinheiro_insuficiente = tela_dinheiro_insuficiente.convert()
