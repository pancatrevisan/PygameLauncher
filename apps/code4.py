import pygame
pygame.init()
tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Titulo da Janela")

sair = False
#definindo a cor
BRANCO = (255,255,255)
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    #limpeza
    janela.fill(BRANCO)
    #atualização dos estados...
    #desenho
    c_cor = (255,0,0)
    pygame.draw.circle(janela, c_cor, (400,300), 200, 0)
    pygame.display.flip()
pygame.quit()  