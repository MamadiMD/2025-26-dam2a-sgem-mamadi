class Rectangulo:
    def __init__(self,x,y,ancho,alto):
        self.__x = x
        self.__y = y
        self.__ancho = ancho
        self.__alto = alto

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto



def intersecting(rectangulo1, rectangulo2):    
    if (rectangulo1.x < rectangulo2.x + rectangulo2.ancho and
        rectangulo1.x + rectangulo1.ancho > rectangulo2.x and
        rectangulo1.y < rectangulo2.y + rectangulo2.alto and
        rectangulo1.y + rectangulo1.alto > rectangulo2.y):
        return True
    else:
        return False
    

a = Rectangulo(20,30,40,40)
b = Rectangulo(50,50,20,20)
c = Rectangulo(30,40,20,20)

print(intersecting(a,b)) 
print(intersecting(a,c)) 
print(intersecting(b,c)) 