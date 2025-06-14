import pygame
class Animation:
    def __init__(self, name):
        self.sprites = []
        self.loop = True
        self.timer = 0
        self.currentSprite = 0
        self.name = name
        self.owner = None
        self.finished = False

    def getCurrentSprite(self):
        return self.sprites[self.currentSprite]
    def setOwner(self, owner):
        self.owner = owner

    def addSprite(self, sprite):
        sprite.setAnimation(self)
        self.sprites.append(sprite)
    
    def update(self, dt):
        #atualiza o timer. Verifica se já passou o tempo do sprite atual.
        #caso tenha passado, vai para o próximo e verifica se é o 
        #último sprite.
        self.timer+=dt
        if(self.timer > self.sprites[self.currentSprite].displayTime):
            self.currentSprite = self.currentSprite + 1
            self.timer = 0
            if(self.currentSprite >= len(self.sprites)):
                if(self.loop):
                    self.currentSprite = 0
                else:
                    self.finished = True
        
    def render(self, dest, onScreenPosition):
        if(self.currentSprite < len(self.sprites)):
            self.sprites[self.currentSprite].render(dest, onScreenPosition)
