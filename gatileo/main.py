import pygame
import random

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
img_rei = pygame.image.load('gatileo/imagens/rato_rei.png').convert_alpha()
img_rei = pygame.transform.smoothscale(img_rei, (50, 50))

fase_2 = pygame.image.load('gatileo/imagens/fase_1beta.png').convert_alpha()
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

contador = pygame.image.load('gatileo/imagens/contador.png').convert_alpha()
contador = pygame.transform.smoothscale(contador, (108, 38))

granada_normal = pygame.image.load("gatileo/imagens/botao_granada.png").convert_alpha()
granada_hover = pygame.transform.smoothscale(granada_normal, (117 - (117//8), 19 - (19//8)))
granada_atual = granada_normal
botao_granada = granada_normal.get_rect(topleft=(163, 321))

icone_granada = pygame.image.load("gatileo/imagens/granada.png").convert_alpha()
icone_granada = pygame.transform.smoothscale(icone_granada, (150, 150))
b_icone_granada = icone_granada.get_rect(topleft=(400, 30))

icone_viratempo = pygame.image.load("gatileo/imagens/viratempo.png").convert_alpha()
icone_viratempo = pygame.transform.smoothscale(icone_viratempo, (150, 150))
b_icone_viratempo = icone_viratempo.get_rect(topleft=(550, 30))

viratempo_normal = pygame.image.load("gatileo/imagens/botao_viratempo.png").convert_alpha()
viratempo_hover = pygame.transform.smoothscale(viratempo_normal, (129 - (129//8), 23 - (23//8)))
viratempo_atual = viratempo_normal
botao_viratempo = viratempo_normal.get_rect(topleft=(350, 318))

interrogacao_normal = pygame.image.load("gatileo/imagens/interrogacao_loja.png").convert_alpha()
interrogacao_normal = pygame.transform.smoothscale(interrogacao_normal, (53, 40))
interrogacao_hover = pygame.transform.scale(interrogacao_normal, (53 - (53//6), 40 - (40//6)))
interrogacao_atual = interrogacao_normal
botao_interrogacao = interrogacao_normal.get_rect(topleft=(70, 365))

voltar_normal = pygame.image.load("gatileo/imagens/botao_voltar.png").convert_alpha()
voltar_hover = pygame.transform.smoothscale(voltar_normal, (142 - (142//5), 48 - (48//5)))
voltar_atual = voltar_normal
botao_voltar = voltar_normal.get_rect(topleft=(88, 80))

tela_inicial_normal = pygame.image.load("gatileo/imagens/botao_tela_inicial.png").convert_alpha()
tela_inicial_hover = pygame.transform.smoothscale(tela_inicial_normal, (221 - (221//5), 36 - (36//5)))
tela_inicial_atual = tela_inicial_normal
botao_tela_inicial = tela_inicial_normal.get_rect(topleft=(270, 259))

jogar_novamente_normal = pygame.image.load("gatileo/imagens/botao_jogar_novamente.png").convert_alpha()
jogar_novamente_hover = pygame.transform.smoothscale(jogar_novamente_normal, (220 - (221//5), 34 - (34//5)))
jogar_novamente_atual = jogar_novamente_normal
botao_jogar_novamente = jogar_novamente_normal.get_rect(topleft=(271, 220))

arma = pygame.Surface([10, 3])

vidas_gato = 3
vida_rei = 25

rato_rei_x = largura//2 - 40
rato_rei_y = altura//2 - 40

tiros_gato = []
balas_inimigas = []

suditos = []

moedas = 0
inventario = []

viratempo_ativo = False
tempo_inicio_viratempo = 0
duracao_viratempo = 10000

texto_moedas = font.render(f'R${moedas}', True, (0, 0, 0))

x_permitidos = [680, 730, 780, 830, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250]
y_permitidos = [100, 150, 200, 250, 300, 350, 400]
ratos_spawnados = 0
total_ratos = 35

ratos = []
def spawnar_ratos():
    global ratos_spawnados
    if ratos_spawnados >= total_ratos:
        return
    x_usados = random.sample(x_permitidos, 6)
    y_usados = random.sample(y_permitidos, 6)
    for i in range (6):
        if ratos_spawnados >= total_ratos:
            break
        x = x_usados[i]
        y = y_usados[i]
        ratos.append([x, y, 0])
        ratos_spawnados = ratos_spawnados + 1

def iniciar_fase_1():
    global ratos_spawnados, ratos_comidos, ratos, parede_do_mapa, pontuacao_alvo
    ratos_spawnados =0
    ratos_comidos =0
    parede_do_mapa = 60
    pontuacao_alvo= 20
    ratos.clear()
    spawnar_ratos()

def iniciar_fase_2():
    global vidas_gato, vida_rei, tiros_gato, balas_inimigas, suditos, y_gato

    y_gato = 225
    gato_rect.y = y_gato
    vidas_gato = 3
    vida_rei = 25

    tiros_gato.clear()
    balas_inimigas.clear()
    suditos.clear()

    suditos.append([420, 50, 1, 0])
    suditos.append([500, 200, 1, 30])
    suditos.append([420, 350, -1, 60])

estado = "tela inicial"

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        if estado == "fase 2":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tiros_gato.append([gato_rect.right, gato_rect.centery])

        if event.type == pygame.MOUSEMOTION:

            if botao_jogar.collidepoint(event.pos):
                jogar_atual = jogar_hover
            else:
                jogar_atual = jogar_normal
            botao_jogar = jogar_atual.get_rect(center = botao_jogar.center)

            if botao_loja.collidepoint(event.pos):
                loja_atual = loja_hover
            else:
                loja_atual = loja_normal
            botao_loja = loja_atual.get_rect(center = botao_loja.center)

            if botao_voltar.collidepoint(event.pos):
                voltar_atual = voltar_hover
            else:
                voltar_atual = voltar_normal
            botao_voltar = voltar_atual.get_rect(center = botao_voltar.center)

            if botao_tela_inicial.collidepoint(event.pos):
                tela_inicial_atual = tela_inicial_hover
            else:
                tela_inicial_atual = tela_inicial_normal
            botao_tela_inicial = tela_inicial_atual.get_rect(center = botao_tela_inicial.center)

            if botao_jogar_novamente.collidepoint(event.pos):
                jogar_novamente_atual = jogar_novamente_hover
            else:
                jogar_novamente_atual = jogar_novamente_normal
            botao_jogar_novamente = jogar_novamente_atual.get_rect(center = botao_jogar_novamente.center)

            if botao_x.collidepoint(event.pos):
                x_atual = x_hover
            else:
                x_atual = x_normal
            botao_x = x_atual.get_rect(center = botao_x.center)

            if botao_xloja.collidepoint(event.pos):
                xloja_atual = xloja_hover
            else:
                xloja_atual = xloja_normal
            botao_xloja = xloja_atual.get_rect(center = botao_xloja.center)

            if botao_granada.collidepoint(event.pos):
                granada_atual = granada_hover
            else:
                granada_atual = granada_normal
            botao_granada = granada_atual.get_rect(center = botao_granada.center)

            if botao_viratempo.collidepoint(event.pos):
                viratempo_atual = viratempo_hover
            else:
                viratempo_atual = viratempo_normal
            botao_viratempo = viratempo_atual.get_rect(center = botao_viratempo.center)

            if botao_interrogacao.collidepoint(event.pos):
                interrogacao_atual = interrogacao_hover
            else:
                interrogacao_atual = interrogacao_normal
            botao_interrogacao = interrogacao_atual.get_rect(center = botao_interrogacao.center)

            if botao_xaviso.collidepoint(event.pos):
                xaviso_atual = xaviso_hover
            else:
                xaviso_atual = xaviso_normal
            botao_xaviso = xaviso_atual.get_rect(center = botao_xaviso.center)

        texto_moedas = font.render(f'R${moedas}', True, (0, 0, 0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if estado == "tela inicial":
                    if botao_jogar.collidepoint(event.pos):
                        estado = "tutorial 1"
                    elif botao_loja.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "fase 2":
                    if b_icone_granada.collidepoint(event.pos):
                        if "granada" in inventario:
                            random_sudito = random.choice(suditos)
                            suditos.remove(random_sudito)
                            inventario.remove("granada")
                    if b_icone_viratempo.collidepoint(event.pos):
                        if "viratempo" in inventario and not viratempo_ativo:
                            viratempo_ativo = True
                            tempo_inicio_viratempo = pygame.time.get_ticks()
                            inventario.remove("viratempo")   
                elif estado == "loja":
                    if botao_voltar.collidepoint(event.pos):
                        estado = "tela inicial"
                    elif botao_interrogacao.collidepoint(event.pos):
                        estado = "tutorial loja"

                    if botao_granada.collidepoint(event.pos):
                        if moedas >= 100:
                            if 'granada' not in inventario:
                                inventario.append('granada')
                                moedas = moedas - 100
                                estado = "comprou granada"
                            else:
                                estado = "granada no inventario"
                        else:
                            estado = 'dinheiro insuficiente'

                    if botao_viratempo.collidepoint(event.pos):
                        if moedas >= 200:
                            if 'viratempo' not in inventario:
                                inventario.append('viratempo')
                                moedas = moedas - 200
                                estado = "comprou viratempo"
                            else:
                                estado = "viratempo no inventario"
                        else:
                            estado = 'dinheiro insuficiente'
                elif estado == "tutorial loja":
                    if botao_xloja.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "comprou granada":
                    if botao_xaviso.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "granada no inventario":
                    if botao_xaviso.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "comprou viratempo":
                    if botao_xaviso.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "viratempo no inventario":
                    if botao_xaviso.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "dinheiro insuficiente":
                    if botao_xaviso.collidepoint(event.pos):
                        estado = "loja"
                elif estado == "tutorial 1":
                    if botao_x.collidepoint(event.pos):
                        estado = "fase 1"
                        iniciar_fase_1()
                elif estado == "derrota":
                    if botao_jogar_novamente.collidepoint(event.pos):
                        estado = "fase 1"
                        iniciar_fase_1()
                    if botao_tela_inicial.collidepoint(event.pos):
                        estado = "tela inicial"
                elif estado == "vitoria":
                    if botao_jogar_novamente.collidepoint(event.pos):
                        estado = "fase 1"
                        iniciar_fase_1()
                    if botao_tela_inicial.collidepoint(event.pos):
                        estado = "tela inicial"
    if estado == "fase 1":    
        teclas = pygame.key.get_pressed()
        velocidade_gato = 5
        velocidade_rato = 3
        if teclas[pygame.K_w]:
            y_gato = y_gato - velocidade_gato
        if teclas[pygame.K_s]:
            y_gato = y_gato + velocidade_gato
        if y_gato < 0:
            y_gato = 0
        if y_gato > altura-50:
            y_gato = altura-50
        gato_rect.y = y_gato
        for rato in ratos.copy():
            rato[0] -= velocidade_rato

            rato [2] += 0.1
            if rato[2]>=len(img_ratos):
                rato[2]= 0
           
            rato_rect = pygame.Rect(rato[0], rato [1], 40,40)
            if rato_rect.colliderect(gato_rect):
                ratos.remove(rato)
                ratos_comidos +=1
            elif rato[0] + 50 < parede_do_mapa:
                ratos.remove(rato)
        if len(ratos) < 6 and ratos_spawnados < total_ratos:
            spawnar_ratos()
        if ratos_spawnados == total_ratos and len(ratos) == 0:
            moedas += 5 * ratos_comidos
            if ratos_comidos >= pontuacao_alvo:
                iniciar_fase_2()
                estado = "fase 2"
            else:
                estado = "derrota"

    if estado == "fase 2":
        teclas = pygame.key.get_pressed()
        velocidade_gato = 5

        if teclas[pygame.K_w]:
            y_gato -= velocidade_gato
        if teclas[pygame.K_s]:
            y_gato += velocidade_gato

        if y_gato < 0:
            y_gato = 0
        if y_gato > altura - 50:
            y_gato = altura - 50

        gato_rect.y = y_gato

        rei_rect = pygame.Rect(rato_rei_x, rato_rei_y, 80, 80)

        for tiro in tiros_gato.copy():
            tiro[0] += 7
            tiro_rect = pygame.Rect(tiro[0], tiro[1], 10, 3)

            if tiro_rect.colliderect(rei_rect):
                tiros_gato.remove(tiro)
                vida_rei -= 1

            elif tiro[0] > largura:
                tiros_gato.remove(tiro)

        for sudito in suditos:

            sudito[1] += 3 * sudito[2]

            if sudito[1] <= 0 or sudito[1] >= altura - 40:
                sudito[2] *= -1

            if not viratempo_ativo:
                if sudito[3] > 0:
                    sudito[3] -= 1
                else:
                    balas_inimigas.append([sudito[0], sudito[1]])
                    sudito[3] = 60

        for bala in balas_inimigas.copy():

            bala[0] -= 5
            bala_rect = pygame.Rect(bala[0], bala[1], 10, 10)

            if bala_rect.colliderect(gato_rect):
                balas_inimigas.remove(bala)
                vidas_gato -= 1

            elif bala[0] < 0:
                balas_inimigas.remove(bala)

        if viratempo_ativo:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - tempo_inicio_viratempo >= duracao_viratempo:
                viratempo_ativo = False

        if vidas_gato <= 0:
            estado = "derrota"

        if vida_rei <= 0:
            estado = "vitoria"

    screen.fill((255, 255, 255))
    
    if estado == "tela inicial":
        screen.blit(tela_inicial, (15, 30))
        screen.blit(titulo, (85, 60))
        screen.blit(jogar_atual, botao_jogar)
        screen.blit(loja_atual, botao_loja)
    elif estado == "tutorial 1":
        screen.blit(tutorial1, (28, 55))
        screen.blit(x_atual, botao_x)
    elif estado == "fase 1":
        x = 20
        y = 20
        screen.blit(fase_1, (0, 0))
        screen.blit(img_gato, (50, y_gato))
        screen.blit(contador, (500, 15))
        txt_contador = font.render(f'{ratos_comidos}/20', True, (0, 0, 0))
        screen.blit(txt_contador, (549, 27))
        for rato in ratos:
            img = img_ratos[int(rato[2])]
            img = pygame.transform.scale(img, (40, 40))
            screen.blit(img, (rato[0], rato[1]))
    elif estado == "tutorial 2":
        screen.blit(tutorial1, (28, 55))
        screen.blit(x_atual, botao_x)
    elif estado == "fase 2":
        screen.blit(fase_2, (0, 0))
        screen.blit(img_gato, (50, y_gato))
        screen.blit(icone_granada, b_icone_granada)
        screen.blit(icone_viratempo, b_icone_viratempo)
        pygame.draw.rect(screen, (120,120,120), (rato_rei_x, rato_rei_y, 80, 80))
        for sudito in suditos:
            pygame.draw.rect(screen, (180,180,180), (sudito[0], sudito[1], 40, 40))
        for tiro in tiros_gato:
            pygame.draw.rect(screen, (0,0,0), (tiro[0], tiro[1], 10, 3))
        for bala in balas_inimigas:
            pygame.draw.rect(screen, (255,0,0), (bala[0], bala[1], 10, 10))
        texto_vidas = font.render(f'Vidas: {vidas_gato}', True, (0,0,0))
        screen.blit(texto_vidas, (10,10))
    elif estado == "loja":
        x_loja = (640 // 2) - tela_loja.get_width() // 2
        y_loja = (480 - tela_loja.get_height()) // 2
        screen.blit(tela_loja, (x_loja, y_loja))
        screen.blit(voltar_atual, botao_voltar)
        screen.blit(interrogacao_atual, botao_interrogacao)
        screen.blit(granada_atual, botao_granada)
        screen.blit(viratempo_atual, botao_viratempo)
        screen.blit(texto_moedas, (475, 95))
    elif estado == "tutorial loja":
        screen.blit(tutorial_loja, (25, 55))
        screen.blit(xloja_atual, botao_xloja)
    elif estado == "comprou granada":
        screen.fill((213, 214, 214))
        screen.blit(tela_comprou_granada, (x_loja + 2, y_loja + 2))
        screen.blit(texto_moedas, (475, 95))
        screen.blit(xaviso_atual, botao_xaviso)
    elif estado == "granada no inventario":
        screen.fill((213, 214, 214))
        screen.blit(tela_granada_inventario, (x_loja + 2, y_loja + 2))
        screen.blit(texto_moedas, (475, 95))
        screen.blit(xaviso_atual, botao_xaviso)
    elif estado == "comprou viratempo":
        screen.fill((213, 214, 214))
        screen.blit(tela_comprou_viratempo, (x_loja + 2, y_loja + 2))
        screen.blit(texto_moedas, (475, 95))
        screen.blit(xaviso_atual, botao_xaviso)
    elif estado == "viratempo no inventario":
        screen.fill((213, 214, 214))
        screen.blit(tela_viratempo_inventario, (x_loja + 2, y_loja + 2))
        screen.blit(texto_moedas, (475, 95))
        screen.blit(xaviso_atual, botao_xaviso)
    elif estado == "dinheiro insuficiente":
        screen.fill((213, 214, 214))
        screen.blit(tela_dinheiro_insuficiente, (x_loja + 2, y_loja + 2))
        screen.blit(texto_moedas, (475, 95))
        screen.blit(xaviso_atual, botao_xaviso)
    elif estado == "vitoria":
        screen.blit(tela_vitoria, (20, 57))
        screen.blit(tela_inicial_atual, botao_tela_inicial)
        screen.blit(jogar_novamente_atual, botao_jogar_novamente)
    elif estado == "derrota":
        screen.blit(tela_derrota, (20, 57))
        screen.blit(tela_inicial_atual, botao_tela_inicial)
        screen.blit(jogar_novamente_atual, botao_jogar_novamente)
        
    pygame.display.flip()
    clock.tick(60)
