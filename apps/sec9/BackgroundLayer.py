import pygame
import math
class BackgroundLayer:
    def __init__(self, imageFile,type, moveSpeed=None):
        self.image = pygame.image.load(imageFile)
        self.moveSpeed = moveSpeed
        self.startPoint = [0,0]
        self.background = None
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.type = type # fill, repeat-x, repeat-y, move
        self.deltaMove = [0,0]

        
        
    def setBackground(self, bkg):
        self.background = bkg

    def update(self, dt):
        w = self.background.getMapWindow()
        self.startPoint = [w[0],w[1]]

        w = self.background.getMapWindow()
        if self.startPoint[0] < 0:
            if (self.startPoint[0] + self.width) < 0:
                self.startPoint[0] = w[2] -1
        if self.startPoint[0] > w[2]-1:
            self.startPoint[0] = 0

        if self.type == "MOVE":
            self.deltaMove[0] += dt * self.moveSpeed[0]
            self.deltaMove[1] += dt * self.moveSpeed[1]
            if self.deltaMove[0] > self.width-1:
                self.deltaMove[0] = 0
            if (self.deltaMove[0] + self.width) < 0:
                self.deltaMove[0] = self.width-1

    def render(self, dest):
        #desenha quantas couberem na tela
        w = self.background.getMapWindow()

        screenW = w[2]
        screenH = w[3]

        if(self.type =='FILL'):
            redim = pygame.transform.scale(self.image, (w[2],w[3])) 
            dest.blit(redim,[0,0])
        elif self.type == "REPEAT-X": #repete em x...
            offsetX = self.startPoint[0]%self.width
            startTileX = math.floor(self.startPoint[0]/self.width)
            endTileX   = math.floor((self.startPoint[0]+screenW)/self.width)

            numTilesX = endTileX - startTileX
            
            #reescala em y....
            redim = pygame.transform.scale(self.image, (self.width,w[3])) 
            print("endx: " +str(endTileX) + " start: " +str(startTileX)+" num Tiles x: " + str(numTilesX))
            #se o bkg for menor que a tela so desenha 1...
            for i in range(0, numTilesX+1):
                dest.blit(redim, [i*self.width -offsetX,0])

        elif self.type == "REPEAT-Y": #repete em y..
            offsetY = self.startPoint[1]%self.height
            numTilesY = math.ceil(self.height/screenH)
            print("offset: " +str(offsetY) + " num tiles y: " +str(numTilesY))
            redim = pygame.transform.scale(self.image, (screenW,self.height)) 
            
            #se o bkg for do tamanho da janela, falta 1. Por isso, + 1.
            if numTilesY == 1:
                numTilesY+= 1
            for i in range(0, numTilesY):
                # -self.heigh, pois o ponto de desenho é o superior esquerdo da imagem,...
                dest.blit(redim, [0,-self.height + screenH - (i*self.height)+offsetY])
                
        elif self.type == "REPEAT": #repete em ambos...
            #para x, mesmo que acima..
            offsetX = self.startPoint[0]%self.width
            startTileX = math.floor(self.startPoint[0]/self.width)
            endTileX   = math.floor((self.startPoint[0]+screenW)/self.width)
            numTilesX = endTileX - startTileX
            
            #para y, mesmo que acima...
            offsetY = self.startPoint[1]%self.height
            numTilesY = math.ceil(self.height/screenH)

            
            
            #se o bkg for do tamanho da janela, falta 1. Por isso, + 1.
            if numTilesY == 1:
                numTilesY+= 1

            for i in range(0, numTilesY):
                for j in range(0, numTilesX+1):
                    # -self.heigh, pois o ponto de desenho é o superior esquerdo da imagem,...
                    dest.blit(self.image, [j*self.width -offsetX,-self.height + screenH - (i*self.height)+offsetY])

        elif self.type =='MOVE': #cenario se move automaticamente.
            #a imagem deve ser maior na direção que vai se mover...
            print(self.deltaMove)
            dest.blit(self.image, [self.deltaMove[0],self.deltaMove[1]])
            if self.deltaMove[0] > 0:
                dest.blit(self.image, [-self.width+self.deltaMove[0],self.deltaMove[1]])
            elif self.deltaMove[0] < 0:
                dest.blit(self.image, [self.deltaMove[0]+self.width,self.deltaMove[1]])

        

