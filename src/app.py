import pygame

pygame.init()
clk = pygame.time.Clock()

size = width, height = 624, 505

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Control NES")
background_image = pygame.image.load('./img/control.png').convert()
frameRect = pygame.Rect((0, 0), (width, height))


crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("white"), (5, 5), 10, 0)


crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)


while True:

    pygame.event.pump()

    screen.blit(background_image, (0, 0))

    Keys = pygame.key.get_pressed()

    # Boton X
    if Keys[pygame.K_z]:
        screen.blit(crosshair, (489, 175))
    # Boton Y
    if Keys[pygame.K_x]:
        screen.blit(crosshair, (429, 221))
    # Boton A
    if Keys[pygame.K_c]:
        screen.blit(crosshair, (548, 221))
    # Boton B
    if Keys[pygame.K_v]:
        screen.blit(crosshair, (489, 268))

    # d-pad arriba
    if Keys[pygame.K_i]:
        screen.blit(crosshair, (130, 190))
    # d-pad abajo
    if Keys[pygame.K_k]:
        screen.blit(crosshair, (131, 256))
    # d-pad izquierda
    if Keys[pygame.K_j]:
        screen.blit(crosshair, (96, 222))
    # d-pad derecha
    if Keys[pygame.K_l]:
        screen.blit(crosshair, (166, 223))
    # Boton Start
    if Keys[pygame.K_SPACE]:
        screen.blit(crosshair, (320, 230))
    # Boton Select
    if Keys[pygame.K_LALT]:
        screen.blit(crosshair, (253, 230))
    # Boton L
    if Keys[pygame.K_LSHIFT]:
        screen.blit(crosshair, (140, 80))
    # Boton R
    if Keys[pygame.K_TAB]:
        screen.blit(crosshair, (482, 80))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(crosshairb, ((x*20)+55-5, (y*20)+125-5))

    pygame.display.flip()

    clk.tick(40)
