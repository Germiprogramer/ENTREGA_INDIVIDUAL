class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def string(self):
        print("({},{})".format(self.x,self.y))
