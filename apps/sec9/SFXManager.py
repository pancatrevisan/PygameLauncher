import pygame
class SFXManager:
    def __init__(self):
        self.sounds = {}

    def play(self, key):
        if key in self.sounds:
            self.sounds[key].play()

    def add(self, key, sound):
        self.sounds[key] = sound