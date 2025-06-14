import pygame
from GameMap import *
from Tileset import *
from PeixeBetta import *

mapa = GameMap(None)
mapa.loadFromFile('map.json')

pygame.init()
tamanhoJanela = [ 800, 600]
resolucaoInterna = [400, 300]
peixe = PeixeBetta()
peixe.setMap(mapa)
peixe.position = [100, 100]
telaParaDesenhar = pygame.Surface((resolucaoInterna[0],resolucaoInterna[1]))
mapa.setWindow([100,0,400,300])

janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")

sair = False
#definindo a cor
BRANCO = (255,255,255)

#cria um objeto do jogo.
clock = pygame.time.Clock()

while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True
            if event.key == pygame.K_ESCAPE:
                sair = True
            elif event.key == pygame.K_RIGHT:
                peixe.andaDireita = True
            elif event.key == pygame.K_LEFT:
                peixe.andaEsquerda = True
            elif event.key == pygame.K_UP:
                peixe.andaCima = True
            elif event.key == pygame.K_DOWN:
                peixe.andaBaixo = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                peixe.andaDireita = False
            elif event.key == pygame.K_LEFT:
                peixe.andaEsquerda = False
            elif event.key == pygame.K_UP:
                peixe.andaCima = False
            elif event.key == pygame.K_DOWN:
                peixe.andaBaixo = False
    
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    peixe.update(dt/1000.0)
    mapa.centerAt(peixe.position)
    #desenho
    
    
    

    #desenho
    mapa.render(telaParaDesenhar)
    peixe.render(telaParaDesenhar)

    #redimensiona a tela de desenho para caber na tela.
    redim = pygame.transform.scale(telaParaDesenhar, (tamanhoJanela[0],tamanhoJanela[1]))    
    janela.blit(redim,[0,0])

    pygame.display.flip()
    
pygame.quit()  