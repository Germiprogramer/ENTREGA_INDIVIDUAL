from classes.punto import *
import math

class Rectangulo():
    def __init__(self, punto_1, punto_2):
        
        self.c_1 = (punto_1.x, punto_1.y)
        self.c_2 = (punto_2.x, punto_1.y)
        self.c_3 = (punto_1.x, punto_2.y)
        self.c_4 = (punto_2.x, punto_2.y)

    def base(self):
        base = abs(self.c_3[0]-self.c_4[0])
        return base

    def altura(self):
        altura = abs(self.c_1[1]-self.c_3[1])
        return altura

    def area(self):
        base = abs(self.c_3[0]-self.c_4[0])
        altura = abs(self.c_1[1]-self.c_3[1])
        area = base * altura
        return area
        

