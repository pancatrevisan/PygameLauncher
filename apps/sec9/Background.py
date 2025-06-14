import pygame
class Background:
    def __init__(self):
        self.layers = []
        self.map = None
    def getMapWindow(self):
        return self.map.getWindow()
    def addLayer(self, layer):
        layer.setBackground(self)
        self.layers.append(layer)
    def setMap(self, map):
        self.map = map
    def update(self, dt):
        for l in self.layers:
            l.update(dt)
    def render(self, dest):
        
        for l in self.layers:
            l.render(dest)