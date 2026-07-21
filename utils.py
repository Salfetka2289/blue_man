import pygame

def load_image(path,size):
    image=pygame.image.load(path)
    image=pygame.transform.scale_by(image,size)
    return(image)

def load_images(path,count,size):
    spritesheet=load_image(path,size)
    W=spritesheet.get_width()
    H=spritesheet.get_height()
    w=W/count
    h=H
    sprites=[]
    x=0
    for i in range(count):
        slise=spritesheet.subsurface(x,0,w,h)
        sprites.append(slise)
        x+=w
    return(sprites)
