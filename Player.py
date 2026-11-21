import animation
import pygame
import lvl
import utils
import goblin
import share
class Player():
    def __init__(self):
        self.x=100
        self.y=100
        self.gravity=0.7
        self.vy=0
        self.time_attack=0
        self.left=False
        self.right=False
        self.size=5
        self.animname='idle'
        self.side='left'
        self.max_jump=2
        self.jumps=2
        self.hp=100
        self.hit_timer=0
        self.death_timer=0
        self.time_in_the_air=0
        self.left_hp=utils.load_image('resourspack/hud elements/health_hud_left.png',3.2)
        self.middle_hp=utils.load_image('resourspack/hud elements/health_hud_middle.png',3.2)
        self.right_hp=utils.load_image('resourspack/hud elements/health_hud_right.png',3.2)
        self.idle=animation.Animation('resourspack/herochar sprites(new)/herochar_idle_anim_strip_4.png',4,self.size)
        self.run=animation.Animation('resourspack/herochar sprites(new)/herochar_run_anim_strip_6.png',6,self.size)
        self.jumpup=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_up_anim_strip_3.png',3,self.size)
        self.jumpdown=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_down_anim_strip_3.png',3,self.size)
        self.double_jump=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_double_anim_strip_3.png',3,self.size)
        self.attack=animation.Animation('resourspack/herochar sprites(new)/herochar_sword_attack_anim_strip_4.png',4,self.size)
        self.hit=animation.Animation('resourspack/herochar sprites(new)/herochar_hit_anim_strip_3.png',3,self.size)
        self.death=animation.Animation('resourspack/herochar sprites(new)/herochar_death_anim_strip_8.png',8,self.size)
        self.anims={
            'run': self.run,
            'idle': self.idle,
            'jumpup': self.jumpup,
            'jumpdown': self.jumpdown,
            'double_jump': self.double_jump,
            'attack': self.attack,
            'hit': self.hit,
            'death': self.death,
        }
    def render(self,skrin):
        if self.animname=='attack' and self.side=='left':
            self.anims[self.animname].render(skrin,self.x-lvl.camerax-90,self.y-lvl.cameray,self.side)
        else:
            self.anims[self.animname].render(skrin,self.x-lvl.camerax,self.y-lvl.cameray,self.side)
        hitbox=self.get_hitbox()
        pygame.draw.rect(skrin,[0,255,0],hitbox.move(-lvl.camerax,-lvl.cameray),3)
        pygame.draw.rect(skrin,[255,0,0],[50,50,265,40])
        pygame.draw.rect(skrin,[0,255,0],[50,50,self.hp*2.65,40])
        skrin.blit(self.left_hp,[45,45])
        x=45+self.left_hp.get_width()
        for i in range(4):
            skrin.blit(self.middle_hp,[x,45])
            x+=self.middle_hp.get_width()
        skrin.blit(self.right_hp,[270,45])
        

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
        if self.time_attack>0:
            self.animname='attack'
            self.time_attack-=1
            player_hitattack=self.get_hitbox_attack()
            for i in goblin.goblins:
                goblin_hitattack=i.hitbox_attack()
                if goblin_hitattack.colliderect(player_hitattack):
                    i.hp-=1.2
                    i.hit_timer=30
        if self.hit_timer>0:
            self.hp-=0.25
            self.animname='hit'
            self.hit_timer-=1

        if self.hp<=0:
            if self.death_timer==0:
                self.death_timer=30
            self.animname='death'
            self.death_timer-=1
            if self.death_timer==0:
                share.load_lvl()

                
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

    def attacks(self):
        self.time_attack=4*5
    
    def get_hitbox_attack(self):
            hitbox=pygame.Rect(self.x,self.y,110,90)   
            return hitbox 
    