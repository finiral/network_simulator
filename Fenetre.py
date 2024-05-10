import pygame
from events.EventHandler import EventHandler
from entity.Serveur import Serveur
from entity.Site import Site
from drawing.ServeurDrawing import ServeurDrawing
import pygame
from events.EventHandler import EventHandler
from entity.Serveur import Serveur
from entity.Site import Site
from drawing.ServeurDrawing import ServeurDrawing

class Fenetre:
    def __init__(self):
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 800

        WHITE = (255, 255, 255)
        BLACK = (60, 60, 60)
        RED = (255, 0, 0)

        FPS = 60

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simulation web")

        # Font initialization
        self.font = pygame.font.SysFont(None, 24)

        self.sites:list[Serveur]
        self.serv = []
        self.servDraw = []

        clock = pygame.time.Clock()
        running = True

        e = EventHandler(self)
        while running:
            self.screen.fill(WHITE) 

            #ETAT FENETRE
            if e.assoc is not None:
                img = self.font.render('mode liaison', True, BLACK)
                self.screen.blit(img, (20, 20))
            if(e.plcrt1 is not None and e.plcrt2 is not None):
                img = self.font.render('mode dijkstra', True, BLACK)
                self.screen.blit(img, (20, 20))
            for event in pygame.event.get():
                isEnd = e.handle_event(event)
                if isEnd:
                    running = False
                    break
            
            #DESSINS DES LIGNES
            for servDraw in self.servDraw:
                center_x, center_y = servDraw.rectangle.center
                for v in servDraw.serveur.getVoisins():
                    vd = self.getServDraw(v[0])
                    if vd:
                        dest_x, dest_y = vd.rectangle.center
                        pygame.draw.line(self.screen, BLACK, (center_x, center_y), (dest_x, dest_y), width=3)
                        mid_x = (center_x + dest_x) // 2
                        mid_y = (center_y + dest_y) // 2
                        poids = v[1]
                        weight_text = str(poids)
                        text_img = self.font.render(weight_text, True, BLACK)
                        self.screen.blit(text_img, (mid_x - text_img.get_width() // 2, mid_y-20 - text_img.get_height() // 2))
                #DESSIN ROUTE DIJKSTRA
                if(e.plcrt1 is not None and e.plcrt2 is not None):
                    s=e.plcrt2
                    spredesc=e.plcrt2.getPredesc()
                    while(spredesc is not None):
                        draw1=self.getServDraw(s)
                        draw2=self.getServDraw(spredesc)
                        center_x, center_y = draw2.rectangle.center
                        dest_x, dest_y = draw1.rectangle.center
                        pygame.draw.line(self.screen, RED, (center_x, center_y), (dest_x, dest_y), width=3)
                        s=spredesc
                        spredesc=s.getPredesc()
                IMAGE = pygame.image.load('dessin_serveur_vrai.png').convert_alpha()
                self.screen.blit(IMAGE, servDraw.rectangle)
                # Draw IP under the image
                ip_text = self.font.render(servDraw.serveur.getIp(), True, BLACK)
                ip_x = servDraw.rectangle.x + (servDraw.rectangle.width - ip_text.get_width()) // 2
                ip_y = servDraw.rectangle.y + servDraw.rectangle.height
                self.screen.blit(ip_text, (ip_x, ip_y))

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        print("FINNNN")


    def getServDraw(self, serveur) -> ServeurDrawing:
        for serv in self.servDraw:
            if serv.serveur == serveur:
                return serv
            
    def getSiteViaServer(self,nomSite) -> Site :
        for serv in self.serv:
            for site in serv.getSites():
                if(site.getDomaine()==nomSite):
                    return site
        return None
    
