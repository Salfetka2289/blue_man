import pygame
import animation
import Player
import lvl
import goblin
import share
import random
pygame.init()
clock=pygame.time.Clock()
skrin=pygame.display.set_mode([0,0])

def load_lvl(): 
    global player
    player=Player.Player()
    lvl.load_hitboxes()
    goblin.load_goblins()

load_lvl()
share.load_lvl=load_lvl
while True:
    clock.tick(60)
    skrin.fill([0,0,0])
    lvl.render(skrin)
    player.render(skrin)
    player.update()
    for i in goblin.goblins:
        i.render(skrin)
        i.update()
        i.control(player)
    if lvl.shake_timer>0:
        lvl.camerax-=random.randint(-lvl.shake_timer,lvl.shake_timer)/2
        lvl.cameray-=random.randint(-lvl.shake_timer,lvl.shake_timer)/2
        lvl.shake_timer-=1
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
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                player.attacks()
    pygame.display.update()

