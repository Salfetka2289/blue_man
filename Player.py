import animation
import pygame
import lvl
class Player():
    def __init__(self):
        self.x=100
        self.y=100
        self.gravity=0.7
        self.vy=0
        self.left=False
        self.right=False
        self.size=5
        self.animname='idle'
        self.side='left'
        self.max_jump=2
        self.jumps=2
        self.time_in_the_air=0
        self.idle=animation.Animation('resourspack/herochar sprites(new)/herochar_idle_anim_strip_4.png',4,self.size)
        self.run=animation.Animation('resourspack/herochar sprites(new)/herochar_run_anim_strip_6.png',6,self.size)
        self.jumpup=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_up_anim_strip_3.png',3,self.size)
        self.jumpdown=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_down_anim_strip_3.png',3,self.size)
        self.double_jump=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_double_anim_strip_3.png',3,self.size)
        self.anims={
            'run': self.run,
            'idle': self.idle,
            'jumpup': self.jumpup,
            'jumpdown': self.jumpdown,
            'double_jump': self.double_jump,
        }
    def render(self,skrin):
        self.anims[self.animname].render(skrin,self.x,self.y,self.side)
        hitbox=self.get_hitbox()
        pygame.draw.rect(skrin,[0,255,0],hitbox,3)

    def update(self):
        self.anims[self.animname].update()
        if self.right==True:
            self.x+=5
            self.collision_x()
            self.animname='run'
            self.side='right'
        if self.left==True:
            self.x-=5
            self.collision_x()
            self.animname='run'
            self.side='left'
        if self.left==False and self.right==False:
            self.animname='idle'
        if self.time_in_the_air>3 and self.vy>0:
            self.animname='jumpup'
        if self.time_in_the_air>3 and self.vy<0:
            self.animname='jumpdown'
        if self.time_in_the_air>3 and self.jumps==0:
            self.animname='double_jump'
        self.vy+=self.gravity
        self.y+=self.vy
        self.time_in_the_air+=1
        self.collision_y()

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
                    self.jumps=self.max_jump
                if self.vy<0:
                    playerhit.top=i.bottom
                    self.vy=0
        self.y=playerhit.y
        
    def get_hitbox(self):
        hitbox=pygame.Rect(self.x,self.y,64,90)   
        return hitbox 

    def jump(self):
        if self.jumps>0:
            self.vy=-13
            self.jumps-=1
        