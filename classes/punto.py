import math

class Punto():
    #contructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #string
    def string(self):
        print("({},{})".format(self.x,self.y))

    #cuadrante
    def cuadrante(self):
        cuadrante = ""
        if self.x == 0 and self.y != 0:
            cuadrante = "eje y"
        elif self.y == 0 and self.x != 0:
            cuadrante = "eje x"
        elif self.y == 0 and self.x == 0:
            cuadrante = "eje coordenadas"
        elif self.x > 0 and self.y > 0:
            cuadrante = "arriba derecha"
        elif self.x < 0 and self.y > 0:
            cuadrante = "arriba izquierda"
        elif self.x < 0 and self.y > 0:
            cuadrante = "abajo derecha"
        elif self.x < 0 and self.y < 0:
            cuadrante = "abajo izquierda"
        print(cuadrante)
        return cuadrante

    #vector
    def vector(self, punto_2):
        v_x = self.x - punto_2.x
        v_y = self.y - punto_2.y
        print("El vector es igual a ({},{})".format(v_x,v_y))
        return (v_x, v_y)

    #distancia
    def distancia(self, punto_2):
        v_x = self.x - punto_2.x
        v_y = self.y - punto_2.y
        distancia = math.sqrt(v_x**2+v_y**2)
        print(distancia)
        return distancia


