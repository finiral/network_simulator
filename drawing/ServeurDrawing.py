import pygame
from entity.Serveur import Serveur
class ServeurDrawing :
    serveur:Serveur
    _isDraging:bool
    def __init__(self,serv,x,y):
        self.x=x
        self.y=y
        self.serveur=serv
        self.rectangle=pygame.rect.Rect(self.x-30, self.y-30, 70, 70)
        self.isDraging=False

