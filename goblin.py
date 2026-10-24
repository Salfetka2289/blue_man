import pygame
import utils
import lvl
import animation
import pytmx
import random
enemes=[]

class Goblin():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.timer=random.randint(30,90)
        self.side='right'
        self.size=5
        self.animname='idle'
        self.left=False
        self.right=False
        self.vy=0
        self.hp=100
        self.gravity=0.7
        self.anims={
            'idle': animation.Animation('resourspack/enemies sprites/goblin/goblin_idle_anim_strip_4.png',4,self.size),
            'run': animation.Animation('resourspack/enemies sprites/goblin/goblin_run_anim_strip_6.png',6,self.size)
        }

    def render(self,skrin):
        self.anims[self.animname].render(skrin,self.x-lvl.camerax,self.y-lvl.cameray,self.side)
        self.hitbox=self.get_hitbox()
        pygame.draw.rect(skrin,(0,0,255),self.hitbox.move(-lvl.camerax,-lvl.cameray),3)
        pygame.draw.rect(skrin,[255,0,0],[self.x-lvl.camerax-20,self.y-lvl.cameray-10,100,10])
        pygame.draw.rect(skrin,[0,255,0],[self.x-lvl.camerax-20,self.y-lvl.cameray-10,self.hp,10])

    def update(self):
        self.anims[self.animname].update()
        if self.left==True:
            self.x-=5
            self.collision_x()
            self.animname='run'
        if self.right==True:
            self.x+=5
            self.collision_x()
            self.animname='run'
        if self.left==False and self.right==False:
            self.animname='idle'
        self.vy+=self.gravity
        self.y+=self.vy
        self.collision_y()

    def get_hitbox(self):
        return pygame.Rect(self.x,self.y,50,80)

    def collision_x(self):
        playerhit=self.get_hitbox()
        for i in lvl.hitboxes:
            if i.colliderect(playerhit):
                if self.side=='right':
                    playerhit.right=i.left
                if self.side=='left':
                    playerhit.left=i.right
        self.x=playerhit.x

    def collision_y(self):
        playerhit=self.get_hitbox()
        for i in lvl.hitboxes:
            if i.colliderect(playerhit):
                if self.vy>0:
                    playerhit.bottom=i.top
                    self.vy=0
                    self.time_in_the_air=0
                if self.vy<0:
                    playerhit.top=i.bottom
                    self.vy=0
        self.y=playerhit.y

    def control(self):
        self.timer-=1
        if self.timer==0:
            if self.animname=='idle':
                rand=random.randint(1,2)
                if rand==1:
                    self.left=True
                    self.side='left'
                else:
                    self.right=True
                    self.side='right'
            else:
                self.left=False
                self.right=False
            self.timer=random.randint(30,90)

def load_goblins():
    card=pytmx.load_pygame('tyled/безымянный.tmx')
    for i in card.get_layer_by_name('goblins'):
        if i[2]!=0:
            goblin=Goblin(i[0]*32*2,i[1]*32*2)
            enemes.append(goblin)



