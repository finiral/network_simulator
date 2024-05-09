from __future__ import annotations
from entity.Site import Site
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
class Serveur :
    _ip:str
    _voisins:list[tuple[Serveur,int]]
    _sites:list[Site]
    _predesc:Serveur
    _distance:int

    def getIp(self):
        return self._ip
    def getVoisins(self) -> list[tuple[Serveur,int]]:
        return self._voisins
    def getSites(self):
        return self._sites
    def getPredesc(self):
        return self._predesc
    def getDistance(self):
        return self._distance
    
    def setIp(self,ip:str):
        self._ip=ip
    def setDistance(self,distance:int):
        self._distance=distance
    def setPredesc(self,predesc:Serveur):
        self._predesc=predesc
    def setVoisins(self,voisins:list[tuple[Serveur,int]]):
        self._voisins=voisins
    def addVoisin(self,voisin:tuple[Serveur,int]):
        self._voisins.append(voisin)
    def setSites(self,sites:list[Site]):
        self._sites=sites
    def addSite(self,site:Serveur):
        self._sites.append(site)

    def __init__(self,ip:str,voisins:list[tuple[Serveur,int]],sites:list[Site]):
        self.setIp(ip)
        self.setVoisins(voisins)
        self.setSites(sites)

    def formDetailServer(self):
        root = tk.Tk()
        root.title(f"Détails du Serveur {self._ip}")
        # Zone de texte pour afficher les sites
        txt_sites = scrolledtext.ScrolledText(root, height=10, width=50)
        txt_sites.pack(pady=10)
        for site in self.getSites():
            txt_sites.insert(tk.END, f"{site.getDomaine()}\n")
        txt_sites.config(state=tk.DISABLED)  # Désactive l'édition

        # Champ de saisie pour ajouter un nouveau site
        site_entry = tk.Entry(root, width=50)
        site_entry.pack(pady=10)

        def add_site():
            site_name = site_entry.get()
            if site_name:  # Vérifie que le champ n'est pas vide
                new_site = Site(site_name)
                self.addSite(new_site)
                site_entry.delete(0, tk.END)  # Efface l'entrée
                txt_sites.config(state=tk.NORMAL)
                txt_sites.insert(tk.END, f"{site_name}\n")
                txt_sites.config(state=tk.DISABLED)
            else:
                messagebox.showinfo("Erreur", "Le nom du site ne peut pas être vide.")

        add_button = tk.Button(root, text="Ajouter Site", command=add_site)
        add_button.pack(pady=5)

        def find_shortest_path():
            # Placeholder pour la logique de recherche du plus court chemin
            messagebox.showinfo("Recherche", "Recherche du chemin le plus court non implémentée.")

        path_button = tk.Button(root, text="Recherche plus court chemin", command=find_shortest_path)
        path_button.pack(pady=10)

        root.mainloop()


