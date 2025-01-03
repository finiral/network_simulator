from math import inf
from entity.Serveur import Serveur
from entity.Site import Site

class Algo:
    @staticmethod
    def getMin(graphe:list[Serveur]) -> Serveur:
        if not graphe:
            return None 
        serveur_min = min(graphe, key=lambda serveur: serveur.getDistance())
        return serveur_min
    
    @staticmethod
    def extractMin(graphe:list[Serveur]) -> Serveur:
        minimal=Algo.getMin(graphe)
        graphe.remove(minimal)
        return minimal
    

    @staticmethod
    def BFS(graphe:list[Serveur],debut:Serveur):
        for sommet in graphe :
            sommet.setDistance(inf)
            sommet.setPredesc(None)
        debut.setDistance(0)
        debut.setVisited(True)
        fil=[]
        fil.append(debut)
        i=1
        while len(fil)!=0:
            v=fil.pop(0)
            for voisin in v.getVoisins():
                if voisin[0].getVisited()==False :
                    voisin[0].setDistance(i)
                    print(i)
                    voisin[0].setVisited(True)
                    voisin[0].setPredesc(v)
                    fil.append(voisin[0])
            i=i+1

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

        
    @staticmethod
    def shortestPathToSite(graphe: list[Serveur], debut: Serveur, site: Site) -> tuple:
        Algo.dijkstra(graphe, debut)
        #liste de tous les serverus avec le site donné
        servWithSite = [serveur for serveur in graphe if site in serveur.getSites()]
        if servWithSite:
            serveur_plus_proche = min(servWithSite, key=lambda s: s.getDistance())
            return serveur_plus_proche
        else:
            return None
        

    @staticmethod
    def shortestPathBFS(graphe: list[Serveur], debut: Serveur, site: Site) -> tuple:
        Algo.BFS(graphe,debut)
        #liste de tous les serverus avec le site donné
        servWithSite = [serveur for serveur in graphe if site in serveur.getSites()]
        if servWithSite:
            serveur_plus_proche = min(servWithSite, key=lambda s: s.getDistance())
            return serveur_plus_proche
        else:
            return None
    
