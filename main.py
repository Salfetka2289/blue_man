import pygame
import animation
import Player
pygame.init()
clock=pygame.time.Clock()
skrin=pygame.display.set_mode([0,0],pygame.FULLSCREEN)
player=Player.Player()
while True:
    clock.tick(60)
    skrin.fill([0,0,0])
    player.render(skrin)
    player.update()
    ivents=pygame.event.get()
    for i in ivents:
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_d:
                player.right=True
            if i.key==pygame.K_a:
                player.left=True
            if i.key==pygame.K_ESCAPE:
               exit()
    pygame.display.update()

