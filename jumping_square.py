import pygame
import random

pygame.init()

CZARNY    = (  0,  0,  0)
BIALY     = (255,255,255)
ZIELONY   = (  0,255,  0)
CZERWONY  = (255,  0,  0)
NIEBIESKI = (  0,  0,255)

rozmiar = (400, 600)
ekran = pygame.display.set_mode(rozmiar)

pygame.display.set_caption("Taktyczny kwadrat")

koniec = False

zegar = pygame.time.Clock()

class Kwadrat():
    def __init__(self):
        self.x=175
        self.y=400
        self.vx=0
        self.vy = 0

    def rysuj(self):
        pygame.draw.rect(ekran, CZARNY, [self.x, self.y, 30, 30])

    def spadaj(self):
        if self.vy < 10:
            self.vy += 1

    def przesun(self):
        self.y += self.vy
        self.x += self.vx

    def odbij(self):
        self.vy = -20


class Deseczka():
    def __init__(self, x, y, szer):
        self.x = x
        self.y = y
        self.szer = szer

    def rysuj(self):
        pygame.draw.rect(ekran, CZARNY, [self.x, self.y, self.szer, 10])

def przesunEkran():
    if kwadrat.y < 250:
        kwadrat.y += 1
        for i in platformy:
            i.y += 1
    if kwadrat.y < 200:
        kwadrat.y += 1
        for i in platformy:
            i.y += 1
    if kwadrat.y < 150:
        kwadrat.y += 1
        for i in platformy:
            i.y += 1

        # ======instancje=====

kwadrat = Kwadrat()
platformy = []
platforma = Deseczka(0, 550, 400)
platformy.append(platforma)
for i in range(100):
    szerokosc = random.randrange(50, 150)
    platforma = Deseczka(random.randrange(0, 400 - szerokosc), 450 - 100 * i, szerokosc)
    platformy.append(platforma)

while not koniec:
    for event in pygame.event.get():  # pętla sprawdzająca listę zdarzeń w pygame
        # jeżeli zdarzenie jest wyjściem z programu
        if event.type == pygame.QUIT:
            koniec = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                kwadrat.vx = -8
            if event.key == pygame.K_d:
                kwadrat.vx = 8
        elif event.type == pygame.KEYUP:
            kwadrat.vx = 0
    kwadrat.spadaj()
    kwadrat.przesun()
    for i in platformy:
        if kwadrat.vy > 0:
            for i in platformy:
                if kwadrat.y + 30 > i.y and kwadrat.y + 18 < i.y:
                    if kwadrat.x + 30 > i.x and kwadrat.x < i.x + i.szer:
                        kwadrat.odbij()

    przesunEkran()
    ekran.fill(BIALY)
    kwadrat.rysuj()
    for i in platformy:
        i.rysuj()
    pygame.display.flip()

    zegar.tick(40)

pygame.quit()
