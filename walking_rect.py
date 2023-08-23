import pygame

pygame.init()

CZARNY = (0, 0, 0)
BIAŁY = (255, 255, 255)
ZIELONY = (0, 255, 0)
CZERWONY = (255, 0, 0)
NIEBIESKI = (0, 0, 255)

rozmiar = (700, 500)
ekran = pygame.display.set_mode(rozmiar)

pygame.display.set_caption("Moja gra")

koniec = False

zegar = pygame.time.Clock()

pozX = 0
pozY = 0

while not koniec:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniec = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pozX += 10
            elif event.key == pygame.K_a:
                pozX -= 10
            elif event.key == pygame.K_s:
                pozY += 10
            elif event.key == pygame.K_w:
                pozY -= 10

    ekran.fill(BIAŁY)

    pygame.draw.rect(ekran, CZERWONY, [pozX, pozY, 20, 20], 2)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    tekst = font.render(f'X: {pozX}, Y: {pozY}', True, NIEBIESKI)
    ekran.blit(tekst, [520, 10])

    pygame.display.flip()

    zegar.tick(60)
pygame.quit()
