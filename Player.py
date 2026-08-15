import animation
class Player():
    def __init__(self):
        self.x=100
        self.y=100
        self.left=False
        self.right=False
        self.idle=animation.Animation('resourspack/herochar sprites(new)/herochar_idle_anim_strip_4.png',4,5)
    def render(self,skrin):
        self.idle.render(skrin,self.x,self.y)
    def update(self):
        self.idle.update()
        if self.right==True:
            self.x+=0.5
        if self.left==True:
            self.x-=0.5