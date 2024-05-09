import pygame
import threading
import tkinter as tk
from tkinter import simpledialog

from drawing.ServeurDrawing import ServeurDrawing
from entity.Serveur import Serveur

class EventHandler:
    def __init__(self, fenetre):
        from Fenetre import Fenetre
        self.assoc:Serveur
        self.assoc=None
        self.fenetre:Fenetre
        self.fenetre = fenetre
        self.offset_x = 0
        self.offset_y = 0
        self.current_dragging = None

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                for servdraw in self.fenetre.servDraw:
                    if servdraw.rectangle.collidepoint(event.pos):
                        self.current_dragging = servdraw
                        servdraw.isDraging = True
                        mouse_x, mouse_y = event.pos
                        self.offset_x = servdraw.rectangle.x - mouse_x
                        self.offset_y = servdraw.rectangle.y - mouse_y
                        return
                threading.Thread(target=lambda:(self.formAddServer(event.pos[0],event.pos[1])),daemon=True).start()
            if event.button==3:
                for servdraw in self.fenetre.servDraw:
                    if servdraw.rectangle.collidepoint(event.pos):
                        if(self.assoc==None):
                            self.setAssoc(servdraw.serveur)
                            print(f"association serveur :{self.assoc}")
                        else:
                            threading.Thread(target=lambda:(self.linkServeur(self.assoc,servdraw.serveur)),daemon=True).start()
                            self.setAssoc(None)

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.current_dragging:
                self.current_dragging.isDraging = False
                self.current_dragging = None

        elif event.type == pygame.MOUSEMOTION:
            if self.current_dragging and self.current_dragging.isDraging:
                mouse_x, mouse_y = event.pos
                self.current_dragging.rectangle.x = mouse_x + self.offset_x
                self.current_dragging.rectangle.y = mouse_y + self.offset_y

        elif event.type == pygame.KEYDOWN:
            for servdraw in self.fenetre.servDraw:
                if event.key==pygame.K_e and servdraw.rectangle.collidepoint(pygame.mouse.get_pos()):
                    threading.Thread(target=lambda:(servdraw.serveur.formDetailServer()),daemon=True).start()


    def formAddServer(self,x,y):
        root = tk.Tk()
        root.withdraw()

        server_name = simpledialog.askstring("New server", "Entrez l'IP de votre serveur:                       ", parent=root)

        if server_name:
            print(f"Server IP entered: {server_name}")
            toAdd=Serveur(server_name,[],[])
            self.fenetre.serv.append(toAdd)
            self.fenetre.servDraw.append(ServeurDrawing(toAdd,x,y))

        root.mainloop()


    def setAssoc(self,serv):
        self.assoc=serv

    def linkServeur(self,serv1:Serveur,serv2:Serveur):
        root = tk.Tk()
        root.withdraw()

        poids = simpledialog.askstring("Link serveur", "Entrez le poids de la liaison:                       ", parent=root)

        if poids:
            print(f"Poids entree: {poids}")
            serv1.addVoisin((serv2,poids))
        root.mainloop()