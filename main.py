import pygame
pygame.init()
clock=pygame.time.Clock()
skrin=pygame.display.set_mode([0,0],pygame.FULLSCREEN)

while True:
    clock.tick(60)
    skrin.fill([0,0,0])
    ivents=pygame.event.get()
    for i in ivents:
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_ESCAPE:
               exit()
    pygame.display.update()

