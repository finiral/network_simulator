from tkinter import messagebox, scrolledtext
import pygame
import threading
import tkinter as tk
from tkinter import simpledialog

from algos.Algo import Algo
from drawing.ServeurDrawing import ServeurDrawing
from entity.Serveur import Serveur
from entity.Site import Site

class EventHandler:
    def __init__(self, fenetre):
        from Fenetre import Fenetre
        self.plcrt1:Serveur
        self.plcrt1=None
        self.plcrt2:Serveur
        self.plcrt2=None
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
                
                if(self.plcrt1 is not None and self.plcrt2 is not None):
                    self.plcrt2=None
                    self.plcrt1=None
                else :
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
                    test=threading.Thread(target=lambda:(self.formDetailServer(servdraw.serveur)),daemon=True).start()
                    if(test==1):
                        print("METI LELEEE")


    def formAddServer(self,x,y):
        root = tk.Tk()
        root.withdraw()

        server_name = simpledialog.askstring("New server", "Entrez l'IP de votre serveur:                       ", parent=root)

        if server_name:
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
            serv1.addVoisin((serv2,int(poids)))
        root.mainloop()

    def formDetailServer(self,serv):
        root = tk.Tk()
        root.title(f"Détails du Serveur {serv._ip}")
        # Zone de texte pour afficher les sites
        txt_sites = scrolledtext.ScrolledText(root, height=10, width=50)
        txt_sites.pack(pady=10)
        for site in serv.getSites():
            txt_sites.insert(tk.END, f"{site.getDomaine()}\n")
        txt_sites.config(state=tk.DISABLED)  # Désactive l'édition
        # Champ de saisie pour ajouter un nouveau site
        site_entry = tk.Entry(root, width=50)
        site_entry.pack(pady=10)
        def add_site():
            site_name = site_entry.get()
            if site_name:  # Vérifie que le champ n'est pas vide
                new_site=self.fenetre.getSiteViaServer(site_name)
                if new_site is None:
                    print("Nouveau site ajouté !")
                    new_site = Site(site_name)
                serv.addSite(new_site)
                site_entry.delete(0, tk.END)  # Efface l'entrée
                txt_sites.config(state=tk.NORMAL)
                txt_sites.insert(tk.END, f"{site_name}\n")
                txt_sites.config(state=tk.DISABLED)
            else:
                messagebox.showinfo("Erreur", "Le nom du site ne peut pas être vide.")

        add_button = tk.Button(root, text="Ajouter Site", command=add_site)
        add_button.pack(pady=5)
        # Champ de saisie pour nom de site a chercher pour dijkstra
        siterecherche = tk.Entry(root, width=50)
        siterecherche.pack(pady=10)
        def find_shortest_path(): 
            nomsite=siterecherche.get()
            if nomsite:   
                toSearch=self.fenetre.getSiteViaServer(nomsite) 
                self.plcrt1=serv
                self.plcrt2=Algo.shortestPathToSite(self.fenetre.serv,self.plcrt1,toSearch)
                root.destroy()
            else:
                messagebox.showinfo("Erreur", "Le nom du site a chercher ne peut pas être vide.")
        path_button = tk.Button(root, text="Recherche plus court chemin", command=find_shortest_path)
        path_button.pack(pady=10)
        root.mainloop()



