
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    cord_1 = Coordenada(2,2)
    cord_2 = Coordenada(1,1)
    #print(cord_1.distancia(cord_2))
    # Para saber si pertenece a la instancia realizamos lo siguiente
    print(isinstance(cord_1, Coordenada))