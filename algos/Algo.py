from math import inf
from entity.Serveur import Serveur
from entity.Site import Site

class Algo:
    @staticmethod
    def getMin(graphe:list[Serveur]) -> Serveur:
        res=graphe[0]
        for serveur in graphe:
            if(res.getDistance()<serveur.getDistance()):
                res=serveur
        return res
    
    @staticmethod
    def extractMin(graphe:list[Serveur]) -> Serveur:
        minimal=Algo.getMin(graphe)
        graphe.remove(minimal)
        return minimal
    
    @staticmethod
    def dijkstra(graphe:list[Serveur],debut:Serveur):
        for sommet in graphe :
            sommet.setDistance(inf)
            sommet.setPredesc(None)
        debut.setDistance(0)
        E=[]
        dupli_graphe=graphe.copy()
        while len(dupli_graphe)!=0:
            minimal=Algo.extractMin(dupli_graphe)
            E.append(minimal)
            for voisin in minimal.getVoisins():
                if(voisin[0].getDistance()>minimal.getDistance()+voisin[1]):
                    voisin[0].setDistance(minimal.getDistance()+voisin[1])
                    voisin[0].setPredesc(minimal)            
    
    
