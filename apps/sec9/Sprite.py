import pygame
from CollisionBox import *

class Sprite:
    def __init__(self, imageFile, displayTime, owner = None, animation = None):
        self.image = pygame.image.load(imageFile)
        self.displayTime = displayTime
        self.animation = animation
        #posicao que será usada para desenhar o sprite.
        #por padrão, o meio do sprite
        self.alignPosition = [int(self.image.get_width()/2), int(self.image.get_height())]
        self.collisionBox = CollisionBox([0,0,self.image.get_width(), self.image.get_height()], self)

    def imageOnWorldPosition(self):
        wP = self.onWorldPosition()
        
        return [wP[0]-self.alignPosition[0], wP[1]-self.alignPosition[1] + self.getHeight()]

    def onWorldPosition(self):
        return self.animation.owner.position

    def getCollisionBox(self):
        return self.collisionBox

    def getAlign(self):
        return self.alignPosition

    def setAnimation(self, animation):
        self.animation = animation

    def getWidth(self):
        return self.image.get_width()

    def getHeight(self):
        return self.image.get_height()
    
    #desenha o sprite na posicao (na surface) informada (onscreenPosition)
    def render(self, dest, onScreenPosition):
        dest.blit(self.image, onScreenPosition)
        rect = self.collisionBox.computeTranslated()
        print("spr: " +str(rect))
        #print("---------------------------------------------------")
        ##print("world pos: " + str(self.animation.owner.position))
        #print("img world: " +str(self.imageOnWorldPosition()))
        #print("colli box: " + str(rect))

        
        rect = self.collisionBox.computeOnScreen()
        
        #para testes, desenha a caixa de colisao na tela.
        pygame.draw.rect(dest, (255,0,0), rect, 1)

    

    

