import pygame
import animation
import Player
import lvl
pygame.init()
clock=pygame.time.Clock()
skrin=pygame.display.set_mode([0,0])
player=Player.Player()
lvl.load_hiboxes()
while True:
    clock.tick(60)
    skrin.fill([0,0,0])
    lvl.render(skrin)
    player.render(skrin)
    player.update()
    ivents=pygame.event.get()
    for i in ivents:
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_d:
                player.right=True
            if i.key==pygame.K_a:
                player.left=True
            if i.key==pygame.K_SPACE:
                player.jump()
            if i.key==pygame.K_ESCAPE:
               exit()
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_d:
                player.right=False
            if i.key==pygame.K_a:
                player.left=False
    pygame.display.update()

