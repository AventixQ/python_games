import pygame

pygame.init()

CZARNY    = (  0,  0,  0)
BIAŁY     = (255,255,255)
ZIELONY   = (  0,255,  0)
CZERWONY  = (255,  0,  0)
NIEBIESKI = (  0,  0,255)

rozmiar = (700, 500)
ekran = pygame.display.set_mode(rozmiar)

pygame.display.set_caption("Arkanoid")

koniec = False

zegar = pygame.time.Clock()

class Pilka:
    def __init__(self):
        self.x = 350
        self.y = 250
        self.vx = 2 #ilość pikseli/jedną klatkę
        self.vy = -2
        self.r = 20
    def rysuj(self):
        pygame.draw.circle(ekran, BIAŁY, [self.x, self.y], self.r)
    def przesun(self):
        self.x += self.vx
        self.y += self.vy
    def sprawdzKolizje(self):
        if self.x - self.r < 0 or self.x + self.r > 700:
            self.vx = - self.vx
        if self.y - self.r < 0 or self.y + self.r > 500:
            self.vy = - self.vy
    def sprawdzKolizjeObiektu(self, xOb, yOb, szerOb, wysOb):
        if (self.x + self.r) > xOb and (self.x - self.r) < (xOb + szerOb) \
                and (self.y + self.r) > yOb and (self.y - self.r) < (yOb + wysOb):
            if (self.y + self.r) < (yOb + 1/4 * wysOb) or (self.y - self.r) > (yOb + 3/4 * wysOb):
                self.vy = -self.vy
            if (self.x + self.r) < (xOb + 1/4 * szerOb) or (self.x - self.r) > (xOb + 3/4 * szerOb):
                self.vx = -self.vx
            return True
        else:
            return False

class Cegla:
    def __init__(self, x, y, kolor):
        self.x = x
        self.y = y
        self.kolor = kolor
        self.szer = 50
        self.wys = 30
    def rysuj(self):
        pygame.draw.rect(ekran, self.kolor, [self.x, self.y, self.szer, self.wys])

class Paletka:
    def __init__(self):
        self.x = 300
        self.y = 400
        self.vx = 0
        self.wys = 20
        self.szer = 100
    def rysuj(self):
        pygame.draw.rect(ekran, CZERWONY, [self.x, self.y, self.szer, self.wys])
    def przesun(self):
        self.x += self.vx

pilka = Pilka()
paletka = Paletka()

mur = []

for i in range(11):
    for j in range(4):
        losowyKolor = ((100 + i * 10), (100 + j * 30), 0)
        cegla = Cegla(30 + 60 * i, 20 + 40 * j, losowyKolor)
        mur.append(cegla)

while not koniec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniec = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                paletka.vx = 5
            if event.key == pygame.K_a:
                paletka.vx = -5
        elif event.type == pygame.KEYUP:
            paletka.vx = 0

    pilka.sprawdzKolizje()
    pilka.przesun()
    paletka.przesun()
    #xOb, yOb, szerOb, wysOb
    pilka.sprawdzKolizjeObiektu(paletka.x, paletka.y, paletka.szer, paletka.wys)

    index = 0
    for i in mur:
        if pilka.sprawdzKolizjeObiektu(i.x, i.y, i.szer, i.wys):
            del mur[index]
            break
        index += 1

    ekran.fill(CZARNY)
    pilka.rysuj()
    paletka.rysuj()
    for i in mur:
        i.rysuj()

    pygame.display.flip()

    zegar.tick(60)

pygame.quit()