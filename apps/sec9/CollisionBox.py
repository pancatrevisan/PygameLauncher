import pygame
class CollisionBox:
    def __init__(self, rect, sprite):
        #o retangulo da cb é com coordenadas dentro da imagem
        # +-----------+
        # | c-------c |
        # | |       | |
        # | c-------c |
        # +-----------+
        self.rect = rect
        self.sprite = sprite
        self.width = self.rect[2]-self.rect[0]
        self.height = self.rect[3] - self.rect[1]
        self.COLLISION_FRONT = 101
        self.COLLISION_LEFT  = 102
        self.COLLISION_BOTTOM = 103
        self.COLLISION_RIGHT  = 104
    def __str__(self):
        return str(self.rect)
    #checa se em algum ponto intersecta outra, mas não verifica
    #os lados
    #https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
    def collides(self, anotherBox):
        if self.rect[0] <  anotherBox.rect[0] + anotherBox.width and self.rect[0] + self.width >  anotherBox.rect[0] and self.rect[1] <  anotherBox.rect[1] + anotherBox.height and self.rect[1] + self.height >  anotherBox.rect[1]:
            return True
        return False
    def isPointInside(self, p):
        tanslated = self
        if p[0] > tanslated.rect[0] and p[0] < (tanslated.rect[0]+ tanslated.width):
            if p[1]>tanslated.rec[1] and p[1] < (tanslated.rect[1] + tanslated.rec[3]):
                return True
        return False
    def checkColType(self, corners):
        coltype = {"LEFT":False, "RIGHT":False, "TOP":False, "BOTTOM":False}
        if corners['topLeft'] and corners['bottomLeft']:
            coltype['LEFT'] = True
        if corners['topLeft'] and corners['topRight']:
            coltype["TOP"] =  True
        if corners['topRight'] and corners['bottomRight']:
            coltype["RIGHT"] =  True
        if corners['bottomLeft'] and corners['bottomRight']:
            coltype["BOTTOM"] =  True

        return coltype

    #verifica se houve colisao e em qual lado da caixa
    def collisionType(self, anotherBox):
        coltype = {}
        #cantos das caixas que estão dentro da outra
        #esta caixa está dentro de anotherBox?
        myCorners = {"topLeft":anotherBox.isPointInside([self.rect[0],self.rect[3]]), 
                "topRight":anotherBox.isPointInside([self.rect[2],self.rect[3]]), 
                "bottomLeft":anotherBox.isPointInside([self.rect[0],self.rect[1]]), 
                "bottomRight":anotherBox.isPointInside([self.rect[2],self.rect[1]])
        }
        #a outra caixa está dentro desta?
        abyCorners = {"topLeft":self.isPointInside((anotherBox.rect[0],anotherBox.rect[3])), 
                "topRight":self.isPointInside((anotherBox.rect[2],anotherBox.rect[3])), 
                "bottomLeft":self.isPointInside((anotherBox.rect[0],anotherBox.rect[1])), 
                "bottomRight":self.isPointInside((anotherBox.rect[2],anotherBox.rect[1]))
        }
        print(myCorners)
        #nenhum intersecta; sem colisão
        if (not myCorners['topLeft']) and (not myCorners['bottomLeft']) and (not myCorners['topRight']) and (not myCorners['bottomRight']):
            coltype['ME'] = "NONE"
            coltype['OTHER'] = "NONE"
            return coltype
        #A está dentro de B
        if myCorners['topLeft'] and myCorners['bottomLeft'] and myCorners['topRight'] and  myCorners['bottomRight']:
            coltype['ME'] = "INSIDE"
            coltype['OTHER'] = "OVER"
            return coltype
        #b está dentro de A
        if abyCorners['topLeft'] and abyCorners['bottomLeft'] and abyCorners['topRight'] and  abyCorners['bottomRight']:
            coltype['ME'] = "OVER"
            coltype['OTHER'] = "INSIDE"
            return coltype
        #verifica os lados
        aCol = self.checkColType(myCorners)
        bCol = self.checkColType(abyCorners)
        ret = {"ME":aCol, "OTHER": bCol}

        

        return ret

    
    def computeOnScreen(self):
        #necessario o acesso à janela do mapa...
        w =self.sprite.animation.owner.map.window#[0,0,800,600] #mudar pela do mapa.
        tBox = self.computeTranslated().rect
        box_h = self.height
        box_w = self.width
        onScreenRect = [int(tBox[0]-w[0]), int(w[3] - tBox[1] - box_h),
        int(box_w), int(box_h)]
        #print("colBox: " +str(onScreenRect))
        return onScreenRect


    #calcula as coordenadas em coordenadas do mundo; a caixa de 
    #colisao está em coordenada na imagem (0 - W, 0 - H)
    def computeTranslated(self):
        spriteOnWorld = self.sprite.imageOnWorldPosition()
        tPos = [spriteOnWorld[0] + self.rect[0],
                spriteOnWorld[1] + self.rect[1],
                spriteOnWorld[0] + self.rect[2],
                spriteOnWorld[1] + self.rect[3]]
        
        
        return CollisionBox(tPos,self.sprite)    

