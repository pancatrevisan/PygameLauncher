import pygame
import json
import subprocess 
button_left = None
button_right = None 
button_confirm = None
button_cancel = None
apps = None
current_app = -1



pygame.init()
tamanhoJanela = [ 800, 600]
telaParaDesenhar = pygame.Surface((tamanhoJanela[0],tamanhoJanela[1]))
janela = pygame.display.set_mode(tamanhoJanela)
pygame.display.set_caption("Eventos de Teclado")
BRANCO = (255,255,255)

clock = pygame.time.Clock()

font = pygame.font.Font(None , 24)

def run_commands(cmd):
    for c in cmd:
        print(c)

def save_joy_conf():
    print(button_left, button_right, button_confirm, button_cancel)
    confs = {
        "button_left" : button_left,
        "button_right" : button_right,
        "button_confirm" : button_confirm,
        "button_cancel" : button_cancel
    }
    with open("confs.json", "w") as file:
        json.dump(confs, file, indent=4)

    


#loop de config do joy/teclado
def config_joy():
    global button_left, button_right, button_confirm, button_cancel
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
    button_left = button_ids[0]
    button_right = button_ids[1]
    button_confirm = button_ids[2]
    button_cancel = button_ids[3]
    save_joy_conf()
    


def load_or_config_joy():
    global button_cancel, button_confirm, button_left, button_right
    try:
        f = open("confs.json", "r")
        f.close()
        with open('confs.json', 'r') as file:
            data = json.load(file)
        button_left = data['button_left']
        button_right = data['button_right']
        button_confirm = data['button_confirm']
        button_cancel = data['button_cancel']
        print(button_left, button_right, button_confirm, button_cancel)

    except:
        print("Config does not exist")
        config_joy()


def load_apps():
    apps = []
    tmp = []
    with open('apps.json', 'r') as file:
        apps = json.load(file)
    

    for a in apps:
    
        apps[a]['bitmap'] = pygame.image.load(apps[a]['background'])
        tmp.append(apps[a])
        

    return tmp


load_or_config_joy()


apps = load_apps()
if len(apps) > 0:
    current_app = 0
print(apps)

sair = False
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        elif event.type == pygame.KEYUP:
            if(event.key == button_left):
                current_app = current_app - 1
                if(current_app < 0):
                    current_app = len(apps) -1
            elif event.key == button_right:
                current_app = current_app + 1
                if current_app >= len(apps):
                    current_app = 0
    #limpeza
    janela.fill(BRANCO)
    telaParaDesenhar.fill(BRANCO)
    dt = clock.tick(30)    
    #limpeza
    janela.fill(BRANCO)
    
    if current_app >=0:
        telaParaDesenhar.blit(apps[current_app]['bitmap'], [0,0])
    
    janela.blit(telaParaDesenhar, [0,0])

    pygame.display.flip()
    
pygame.quit()  