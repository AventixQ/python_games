import pygame
import random

pygame.init()

CZARNY = (0, 0, 0)
BIAŁY = (255, 255, 255)
ZIELONY = (0, 255, 0)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)
ŻÓŁTY = (255, 255, 0)
RÓŻOWY = (255, 0 ,196)
LAWENDOWY = (100, 40, 202)
POMARAŃCZ = (255, 100, 33)

rozmiar = (700, 500)
ekran = pygame.display.set_mode(rozmiar)

pygame.display.set_caption("Kwiatkuszki")

koniec = False

zegar = pygame.time.Clock()

def rysujKwiat(x,y,kolor):
    pygame.draw.rect(ekran, ZIELONY, [x,y,6,40],3)
    for i in [-14,14]:
        for j in [-14,14]:
            pygame.draw.circle(ekran, kolor, [x+3+i, y-20+j], 15)
    pygame.draw.circle(ekran, ŻÓŁTY, [x+3, y-20],10)

for barwa in [CZERWONY, NIEBIESKI, RÓŻOWY, POMARAŃCZ, LAWENDOWY]:
    for nr in range(10):
        rysujKwiat(random.randrange(20,680),random.randrange(20,480), barwa)

while not koniec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniec = True

    pygame.display.flip()

    zegar.tick(60)
pygame.quit()
