import animation
class Player():
    def __init__(self):
        self.x=100
        self.y=100
        self.gravity=0.75
        self.vy=0
        self.left=False
        self.right=False
        self.size=5
        self.animname='idle'
        self.side='left'
        self.idle=animation.Animation('resourspack/herochar sprites(new)/herochar_idle_anim_strip_4.png',4,self.size)
        self.run=animation.Animation('resourspack/herochar sprites(new)/herochar_run_anim_strip_6.png',6,self.size)
        self.jumpup=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_up_anim_strip_3.png',3,self.size)
        self.jumpdown=animation.Animation('resourspack/herochar sprites(new)/herochar_jump_down_anim_strip_3.png',3,self.size)
        self.anims={
            'run': self.run,
            'idle': self.idle,
            'jumpup': self.jumpup,
            'jumpdown': self.jumpdown,
        }
    def render(self,skrin):
       self.anims[self.animname].render(skrin,self.x,self.y,self.side)
    def update(self):
        self.anims[self.animname].update()
        if self.right==True:
            self.x+=5
            self.animname='run'
            self.side='right'
        if self.left==True:
            self.x-=5
            self.animname='run'
            self.side='left'
        if self.left==False and self.right==False:
            self.animname='idle'
        self.vy+=self.gravity
        self.y+=self.vy
        
