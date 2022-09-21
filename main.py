from classes.punto import *
from classes.rectangulo import *

if __name__ == "__main__":
    #puntos
    A = Punto(2,3)
    B = Punto(5,5)
    C = Punto(-3,-1)
    D = Punto(0,0)

    #cuadrantes
    A.cuadrante()
    C.cuadrante()
    D.cuadrante()

    #vectores
    A.vector(B)
    B.vector(A)

    #distancia
    A.distancia(B)

    #distancia más grande
    if A.distancia(D) > B.distancia(D) and A.distancia(D) > C.distancia(D):
        print("A es el más lejano")
    elif B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D):
        print("B es el más lejano")
    elif C.distancia(D) > A.distancia(D) and C.distancia(D) > B.distancia(D):
        print("C es el más lejano")
    else:
        print("hay dos o más distancias iguales")
    
            
    #rectángulo
    r = Rectangulo(A,B)

    base = r.base()
    altura = r.altura()
    area = r.area()
    print("Base = {}, Altura = {}, Área = {}".format(base,altura,area))