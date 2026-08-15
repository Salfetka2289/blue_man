import utils

class Animation:
    def __init__(self,path,count,size):
        self.images=utils.load_images(path,count,size)
        self.index=0
        self.timer=5
    def render(self,skrin,x,y):
        skrin.blit(self.images[self.index],[x,y])
    def update(self):
        self.timer-=1
        if self.timer==0:
            self.index+=1
            self.timer=5
        if self.index==len(self.images):
            self.index=0