import pygame
class Tile:
    def __init__(self, name, image):
        self.image = image
        self.name = name
        #o tile poderá ter mais propriedades...
    
    def getName(self):
        return self.name
    def getImage(self):
        return self.image
