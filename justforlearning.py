import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("Nurlybek game")

running = True

square = pygame.Surface((50,170))
square.fill('Yellow')

myfont = pygame.font.Font('Roboto-Black.ttf',40)
text_surface = myfont.render('your points:',True,'Red')



while running:

    screen.blit(square,(300,150))    
    screen.blit(text_surface,(0,0))
    pygame.draw.circle(screen,'Blue',(250,150),20)

    pygame.display.update()
    
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_a:
                #screen.fill((70,44,133))

    
    


if event.type == INC_SPEED:
            SPEED += 0.5