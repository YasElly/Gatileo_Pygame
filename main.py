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

x_normal = pygame.image.load('gatileo/imagens/x.png').convert_alpha()
x_hover = pygame.transform.smoothscale(x_normal, (42 - (42//5), 42 - (42//5)))
x_atual = x_normal
botao_x = x_normal.get_rect(topleft=(546, 65))

xloja_normal = pygame.image.load('gatileo/imagens/x.png').convert_alpha()
xloja_hover = pygame.transform.smoothscale(xloja_normal, (42 - (42//5), 42 - (42//5)))
xloja_atual = xloja_normal
botao_xloja = xloja_normal.get_rect(topleft=(555, 60))

xaviso_normal = pygame.image.load('gatileo/imagens/x_aviso.png').convert_alpha()
xaviso_hover = pygame.transform.smoothscale(xaviso_normal, (42 - (42//5), 42 - (42//5)))
xaviso_atual = xaviso_normal
botao_xaviso = xaviso_normal.get_rect(topleft=(485, 115))

fase_1 = pygame.image.load('gatileo/imagens/fase_1beta.png').convert_alpha()
fase_1 = pygame.transform.smoothscale(fase_1, (640, 480))
img_ratos = [ 
    pygame.image.load("gatileo/imagens/rato_0.png").convert_alpha(),
    pygame.image.load("gatileo/imagens/rato_1.png").convert_alpha(),
    pygame.image.load("gatileo/imagens/rato_2.png").convert_alpha()
 ] 
img_gato = pygame.image.load('gatileo/imagens/gato.png').convert_alpha()
img_gato = pygame.transform.smoothscale(img_gato, (50, 50))

fase_2 = pygame.image.load('gatileo/imagens/fase_2beta.png').convert_alpha()
fase_2 = pygame.transform.smoothscale(fase_2, (640, 480))

y_gato = 225
q_gato = pygame.Surface([50, 50])
gato_rect = q_gato.get_rect(topleft=(50, y_gato))

tela_vitoria = pygame.image.load("gatileo/imagens/tela_vitoria2.png")
tela_vitoria = tela_vitoria.convert()
tela_vitoria = pygame.transform.smoothscale(tela_vitoria, (640, 366))

tela_derrota = pygame.image.load("gatileo/imagens/tela_derrota2.png")
tela_derrota = tela_derrota.convert()
tela_derrota = pygame.transform.smoothscale(tela_derrota, (640, 366))

jogar_normal = pygame.image.load("gatileo/imagens/botao_jogar.png").convert_alpha()
jogar_hover = pygame.transform.smoothscale(jogar_normal, (221, 51))
jogar_atual = jogar_normal
botao_jogar = jogar_normal.get_rect(topleft=(94, 167))

loja_normal = pygame.image.load("gatileo/imagens/botao_loja.png").convert_alpha()
loja_hover = pygame.transform.smoothscale(loja_normal, (249 - (249//5), 54 - (54//5)))
loja_atual = loja_normal
botao_loja = loja_normal.get_rect(topleft=(93, 253))