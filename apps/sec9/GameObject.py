import pygame
import math
class GameObject:
    def __init__(self, position = [0,0]):
        #posição do personagem. Parte inferior, centralizada no sprite.
        #
        # ---------
        # |        |
        # |        |
        # |____P___|
        self.position = position#posicao no mundo.
        self.animations ={} #animações. um dicionário
        self.currentAnimation = None
        self.map = None
        self.lastMove  = [0,0]

    def setMap(self, map):
        self.map = map
    def getCurrentCollisionBox(self):
        return self.currentAnimation.getCurrentSprite().getCollisionBox()

    def onScreen(self):
        return False

    def collides(self, anotherObject):
        myColl = self.getCurrentCollisionBox().computeTranslated()
        aoColl = anotherObject.getCurrentCollisionBox().computeTranslated()
        print(myColl)
        print(aoColl)
        return myColl.collides(aoColl)

    def checkCollision(self, anotherObject):
        anotherBoxColl = anotherObject.getCurrentCollisionBox().computeTranslated()
        myColl = self.getCurrentCollisionBox().computeTranslated()
        coltype = myColl.collisionType(anotherBoxColl)
        
        return coltype
    def moveTo(self, pos):
        self.lastMove =[pos[0] - self.position[0], pos[1]-self.position[1]]

        self.position = [pos[0], pos[1]]
        cb = self.getCurrentCollisionBox().computeTranslated()
        if cb.rect[0] < 0:
            cb.rect[0] = 0
        if cb.rect[2] >= self.map.widthPixels:
            cb.rect[2] = self.map.widthPixels -1
    def computeBoundTiles(self):
        tSize = self.map.getTileset().getSize()
        cb = self.getCurrentCollisionBox().computeTranslated()
        #print("CB> " + str(cb.rect))
        l = int(cb.rect[0]/tSize)
        u =  int( cb.rect[3]/tSize)
        r = int((cb.rect[2]-1)/tSize)
        b =  int(cb.rect[1]/tSize)
        return {"l":l,"r":r, "u":u,"b":b}    
    def checkMapCollision(self):
        if self.map == None:
            return
        tSize = self.map.getTileset().getSize()
        
        
        
        #verifica se colide em cima e empurra para baixo
        if(self.lastMove[1]>0):
            bounds = self.computeBoundTiles()
            l = bounds['l']
            u =  bounds['u']
            r = bounds['r']
            b =  bounds['b']
            for i in range(l, r+1):
                if self.map.getCell(u, i)!=None:
                    #houve colisão
                    print("colisao topo")
                    self.position =[self.position[0], self.map.window[3] -  (i-1) * tSize - cb.height]
                    break

        #verifica embaixo
        if(self.lastMove[1]<0):
            bounds = self.computeBoundTiles()
            l = bounds['l']
            u =  bounds['u']
            r = bounds['r']
            b =  bounds['b']
            for i in range(l, r+1):
                if self.map.getCell(b, i)!= None:
                    print("colisao baixo")
                    print([l,r,u,b])
                    #houve colisao na parte de baixo
                    inv = self.map.height - b
                    
                    self.position =[self.position[0], (b+1) * tSize ]
                    break
        


        
        if(self.lastMove[0] <0):
        #verifica a esquerda.
            cb = self.getCurrentCollisionBox().computeTranslated()
            bounds = self.computeBoundTiles()
            l = bounds['l']
            u =  bounds['u']
            r = bounds['r']
            b =  bounds['b']
            for i in range(b,u+1):
                if(self.map.getCell(i,l))!=None:
                    print("colisao esquerda")
                    offset = tSize - (cb.rect[0] % tSize) #quao dentro do tile está?
                    print(">>>>Offset: " + str(offset))
                    
                    self.position =[self.position[0]+offset, self.position[1]]
                    break
            
        
        if self.lastMove[0] >0:
            cb = self.getCurrentCollisionBox().computeTranslated()
            bounds = self.computeBoundTiles()
            l = bounds['l']
            u =  bounds['u']
            r = bounds['r']
            b =  bounds['b']
            print([l,r,u,b])
            #verifica a direita
            for i in range(b,u+1):
                if(self.map.getCell(i,r))!=None:
                    print("colisao direita")
                    offset = cb.rect[2] % tSize
                    self.position =[self.position[0]  - offset, self.position[1]]
                    break


    #método de atualização, para ser sobrescrito em subclasses.
    def update(self, dt):
        raise Exception("Implemente o método de atualização :)")
    
    def render(self, dest):
        if self.currentAnimation != None:
            
            worldToScreen = [self.position[0] - self.currentAnimation.getCurrentSprite().getAlign()[0] - self.map.getWindow()[0], 0]
            worldToScreen[1] = self.position[1]+self.currentAnimation.getCurrentSprite().getHeight()
            worldToScreen[1] = self.map.window[3] - worldToScreen[1]
            worldToScreen = [int(worldToScreen[0]), worldToScreen[1]]
            self.currentAnimation.render(dest, worldToScreen)

            #desenha o ponto da posição na tela...
            posToScreen = [int(self.position[0] - self.map.getWindow()[0]), int(self.map.window[3] - self.position[1])]
            pygame.draw.circle(dest,(0,0,0),posToScreen,3)
    def addAnimation(self, animation):
        animation.setOwner(self)
        self.animation[animation.name] = animation