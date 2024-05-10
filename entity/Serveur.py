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
    visited:bool
    visited=False

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
    def getVisited(self):
        return self.visited
    
    def setIp(self,ip:str):
        self._ip=ip
    def setDistance(self,distance:int):
        self._distance=distance
    def setPredesc(self,predesc:Serveur):
        self._predesc=predesc
    def setVoisins(self,voisins:list[tuple[Serveur,int]]):
        self._voisins=voisins
    def setVisited(self,vi):
        self.visited=vi

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
