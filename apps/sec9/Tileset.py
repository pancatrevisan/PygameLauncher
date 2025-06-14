import pygame
from Tile import *
class Tileset:
    def __init__(self, image_file, size, prefix="t_"):
        self.image = pygame.image.load(image_file)
        if self.image.get_width()%size != 0 or self.image.get_height()%size != 0:
            print("ERROR. Size is not compatible with image. ")
            exit()
        if size%2 !=0:
            print("ERROR. Size must be multiple of 2 ")
            exit()
        self.namePrefix = prefix
        self.size = size
        
        self.tiles = {}
        

        cont = 0
        for i in range(0, int(self.image.get_height()/size)): #para altura...
            for j in range(0, int(self.image.get_width()/size)): #para largura
                #retângulo de 'corte'
                rect =[j * self.size, i *self.size, self.size, self.size] 
                #cria uma subsurface, "filha" da imagem original
                subS = self.image.subsurface(rect)
                #novo tile
                t = Tile(prefix+str(cont), subS)
                #dicionario para acesso mais fácil
                self.tiles[t.getName()] = t
                cont+= 1
    def getSize(self):
        return self.size
    def getTile(self, name):
        
        if name in self.tiles:
            return self.tiles[name]
        return None