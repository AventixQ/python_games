import pygame
import random

pygame.init()

CZARNY = (0, 0, 0)
BIAŁY = (255, 255, 255)
ZIELONY = (0, 255, 0)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)

szerokoscOkna = 700
wysokoscOkna = 500
rozmiar = (szerokoscOkna, wysokoscOkna)
ekran = pygame.display.set_mode(rozmiar)

pygame.display.set_caption("Snake")

koniec = False

zegar = pygame.time.Clock()

class Segment:
    def __init__(self):
        self.rozmiar = 19
        self.vxy = [20, 0]
        self.vxyOld = [20, 0]
        self.pos = [300, 200]

    def przesun(self):
        self.pos[0] += self.vxy[0]
        self.pos[1] += self.vxy[1]

    def rysuj(self, kolor):
        pygame.draw.rect(ekran, kolor, [self.pos[0], self.pos[1], self.rozmiar, self.rozmiar])

    def kolizja(self, obiekt):
        if self.pos == obiekt.pos:
            return True
        else:
            return False

waz = []
for i in range(5):
    segment = Segment()
    segment.pos[0] = segment.pos[0] - 20 * i
    waz.append(segment)

punkt = Segment()
punkt.pos = [20 * random.randrange(0,35), 20 * random.randrange(0,25)]

while not koniec:
    for event in pygame.event.get():  # pętla sprawdzająca listę zdarzeń w pygame
        # jeżeli zdarzenie jest wyjściem z programu
        if event.type == pygame.QUIT:
            koniec = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and waz[0].vxy != [-20, 0]:
                waz[0].vxy = [20, 0]
            elif event.key == pygame.K_a and waz[0].vxy != [20, 0]:
                waz[0].vxy = [-20, 0]
            elif event.key == pygame.K_w and waz[0].vxy != [0, 20]:
                waz[0].vxy = [0, -20]
            elif event.key == pygame.K_s and waz[0].vxy != [0, -20]:
                waz[0].vxy = [0, 20]
    indeks = 0
    for i in waz:
        i.vxyOld = i.vxy
        i.przesun()
        if indeks > 0:
            i.vxy = waz[indeks - 1].vxyOld
        indeks += 1

    if waz[0].kolizja(punkt):
        punkt.pos = [20 * random.randrange(0, 35), 20 * random.randrange(0, 25)]
        segL = waz[-1]
        segN = Segment()
        segN.pos[0] = segL.pos[0] - segL.vxyOld[0]
        segN.pos[1] = segL.pos[1] - segL.vxyOld[1]
        segN.vxy = segL.vxyOld
        waz.append(segN)

    for i in range(1, len(waz)):
        if waz[0].kolizja(waz[i]): koniec = True

    if waz[0].pos[0] >= 700 or waz[1].pos[1] >= 500: koniec = True
    if waz[0].pos[0] <= -20 or waz[1].pos[1] <= -20: koniec = True


    ekran.fill(CZARNY)
    q = 1
    for i in waz:
        i.rysuj((q * 10, q * 10, 255))
        q += 2
        if q * 10 > 255: q = 0

    punkt.rysuj(CZERWONY)

    pygame.display.flip()

    zegar.tick(5)

pygame.quit()
