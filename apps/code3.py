import pygame
pygame.init()

tamanhoJanela = [ 800, 600]
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Titulo da Janela")

sair = False
#definindo a cor
VERMELHO = (255,0,0)
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    
    #limpeza
    janela.fill(VERMELHO)
    #atualização dos estados...
    
    #desenho
    rect = [10, 10, 30, 30]
    r_cor = (255,255,255)
    pygame.draw.rect(janela, r_cor, rect)

    #com borda
    #pygame.draw.rect(janela, r_cor, rect,1)

    pygame.display.flip()

pygame.quit()  