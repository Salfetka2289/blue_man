import utils
class Animation:
    def __init__(self,path,count,size):
        images=utils.load_images(path,count,size)
        index=0
        