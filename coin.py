import pygame
import animation
import share
coins=[]
count_coins=0

class Coin():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.size=5
        self.anims={
            'idle':animation.Animation('resourspack/miscellaneous sprites/coin_anim_strip_6.png',6,self.size),
            'picked':animation.Animation('resourspack/miscellaneous sprites/coin_pickup_anim_strip_6.png',6,self.size)
        }
        self.animname='idle'

    def render(self):
        self.anims[self.animname].render()


