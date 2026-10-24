import pygame
import random
pygame.init()
clock=pygame.time.Clock()
skrin=pygame.display.set_mode([1500,1000])
circles=[]
hitcircles=[]
rectx=100
recty=800
left=False
right=False
background=(0,0,0)

def render():
    for i in circles:
        pygame.draw.circle(skrin,[255,255,255],[i[0],i[1]],10)
    pygame.draw.rect(skrin,[200,150,255],[rectx,recty,200,20])

def update():
    global rectx
    for i in circles:
         i[1]+=2
    if left==True:
        rectx-=5
    if right==True:
        rectx+=5

def randoms():
    y=0
    global circles
    x=random.randint(0,1500)
    circles.append([x,y])

def hitboxes():
    global background
    hitrect=pygame.Rect(rectx,recty,200,20)
    for i in circles:
        hitcircle=pygame.Rect(i[0],i[1],10,10)
        if hitcircle.colliderect(hitrect):
            background=(255,0,0)

time=60
while True:
    clock.tick(60)
    skrin.fill(background)
    update()
    render()
    hitboxes()
    time-=1
    if time==0:
        randoms()
        time=60
    get=pygame.event.get()
    for i in get:
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_d:
                right=True
            if i.key==pygame.K_a:
                left=True
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_d:
                right=False
            if i.key==pygame.K_a:
                left=False
            if i.key==pygame.K_ESCAPE:
                       exit()
    pygame.display.update()

