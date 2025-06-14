import pygame
import json

button_left = None
button_right = None 
button_confirm = None
button_cancel = None




pygame.init()
tamanhoJanela = [ 800, 600]
telaParaDesenhar = pygame.Surface((tamanhoJanela[0],tamanhoJanela[1]))
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")
BRANCO = (255,255,255)

clock = pygame.time.Clock()


font = pygame.font.Font(None , 24)

#loop de config do joy/teclado

def config_joy():
    buttons = ["button_left", "button_right", "button_confirm", "button_cancel"]
    button_names = ["Left", "Right", "Confirm", "Cancel"]
    button_ids   = []
    index = 0
    while index < len(buttons):

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print(event)
                button_ids.append(event.key)
                index = index + 1
            elif event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONUP:
                pass
        janela.fill(BRANCO)
        telaParaDesenhar.fill(BRANCO)
        t_color = (0 ,127 ,50)
        if index < len(buttons):
            text = font.render("Press a Key/Joy Button for " + button_names[index], True , t_color )
            telaParaDesenhar.blit(text , [50 ,50])

        janela.blit(telaParaDesenhar,[0,0])
        pygame.display.flip ()
    print(button_ids)
    

def read_joy_conf():
    pass
try:
    f = open("confs.txt", "r")
except:
    print("Config does not exist")
    config_joy()





sair = False
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    

    pygame.display.flip()
    
pygame.quit()  