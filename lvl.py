import utils
import pygame
import pytmx
image=pygame.image.load('tyled/безымянный.png')
image=pygame.transform.scale_by(image,2)

def render(skrin):
    skrin.blit(image,[0,0])
    for i in hitboxes:
        pygame.draw.rect(skrin,[255,0,0],i,3)

hitboxes=[]

def load_hiboxes():
    map=pytmx.load_pygame('tyled/безымянный.tmx')
    for i in map.get_layer_by_name('ground'):
        if i[2]!=0:
            hitbox=pygame.Rect(i[0]*32*2,i[1]*32*2,32*2,32*2)
            hitboxes.append(hitbox)