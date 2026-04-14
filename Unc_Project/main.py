
import pygame
import unc

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
deltatime = 0.0
running = True

dragging = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

onkel = unc.Unc(screen, player_pos, 40)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:	#did the user press X
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False


    # fill the screen with a color
    screen.fill("#FFD543")

    # gameupdate
    if dragging:
        #print(pygame.mouse.get_pos()[0])
        onkel.SetPosition(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    onkel.update(deltatime)



    # here comes the rendering
    onkel.draw()

    # flip() to put the work to screen
    pygame.display.flip()

    deltatime = clock.tick(60) / 1000

pygame.quit()
