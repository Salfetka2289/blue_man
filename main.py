import pygame
import animation
import Player
import lvl
import goblin
pygame.init()
clock=pygame.time.Clock()
skrin=pygame.display.set_mode([0,0])
player=Player.Player()
lvl.load_hiboxes()
goblin.load_goblins()

while True:
    clock.tick(60)
    skrin.fill([0,0,0])
    lvl.render(skrin)
    player.render(skrin)
    player.update()
    for i in goblin.enemes:
        i.render(skrin)
        i.update()
        i.control()
    lvl.camerax+=(player.x-lvl.camerax-skrin.get_width()/2)/20
    lvl.cameray+=(player.y-lvl.cameray-skrin.get_height()/2)/20
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

