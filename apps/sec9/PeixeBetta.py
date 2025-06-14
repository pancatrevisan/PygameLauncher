from GameObject import *
from Animation import *
from Sprite import *
class PeixeBetta(GameObject):
    def __init__(self):
        GameObject.__init__(self)        
        
        #Cria animacao...
        nadaDireita = Animation("nadaDireita")
        nadaDireita.setOwner(self)
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/1.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/2.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/3.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/4.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/5.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/6.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/7.png',200/1000.0,self, nadaDireita))
        nadaDireita.addSprite(Sprite('blue_betta/betta_swim_right/8.png',200/1000.0,self, nadaDireita))

        nadaEsquerda = Animation("nadaEsquerda")
        nadaEsquerda.setOwner(self)
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/1.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/2.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/3.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/4.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/5.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/6.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/7.png',200/1000.0,self, nadaEsquerda))
        nadaEsquerda.addSprite(Sprite('blue_betta/betta_swim_left/8.png',200/1000.0,self, nadaEsquerda))

        #adiciona às animações do Objeto
        self.animations[nadaDireita.name] = nadaDireita
        self.animations[nadaEsquerda.name] = nadaEsquerda
        self.currentAnimation = nadaDireita
        self.velocidade = 100 #100px/s
        self.andaDireita = False
        self.andaEsquerda = False
        self.andaCima = False
        self.andaBaixo = False

    
    def update(self, dt):
        
        newPos = [self.position[0], self.position[1]]
        if self.andaDireita:
            self.currentAnimation = self.animations['nadaDireita']
            newPos[0] = self.position[0] + self.velocidade * dt
            #self.moveTo([, self.position[1]])
        elif self.andaEsquerda:
            self.currentAnimation = self.animations['nadaEsquerda']
            #self.moveTo([, self.position[1]])
            newPos[0] = self.position[0] - self.velocidade * dt
        
        if self.andaCima:
            #self.moveTo([self.position[0], self.position[1] + self.velocidade * dt])
            newPos[1] = self.position[1] + self.velocidade * dt
            
        elif self.andaBaixo:
            #self.moveTo([self.position[0], self.position[1] - self.velocidade * dt])
            newPos[1] = self.position[1] - self.velocidade * dt
            
        self.moveTo(newPos)
        self.currentAnimation.update(dt)
        self.checkMapCollision()
        