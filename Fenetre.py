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
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        FPS = 60

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simulation web")

        self.serv = []
        self.servDraw = []

        clock = pygame.time.Clock()
        running = True

        e = EventHandler(self)
        while running:
            self.screen.fill(WHITE)  # Clear the screen first

            if e.assoc is not None:
                font = pygame.font.SysFont(None, 24)
                img = font.render('mode liaison', True, BLACK)
                self.screen.blit(img, (20, 20))

            for event in pygame.event.get():
                isEnd = e.handle_event(event)
                if isEnd:
                    running = False
                    break

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
                        text_img = font.render(weight_text, True, BLACK)
                        self.screen.blit(text_img, (mid_x - text_img.get_width() // 2, mid_y-20 - text_img.get_height() // 2))

                IMAGE = pygame.image.load('dessin_serveur_vrai.png').convert_alpha()
                self.screen.blit(IMAGE, servDraw.rectangle)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        print("FINNNN")

    def getServDraw(self, serveur) -> ServeurDrawing:
        for serv in self.servDraw:
            if serv.serveur == serveur:
                return serv