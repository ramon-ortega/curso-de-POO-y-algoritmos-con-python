class Automovil:
    def __init__(self, modelo, anio, color, marca):
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.marca = marca
        self._estado = 'resposo'
        self._motor = None

    def acelera(self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)


class Motor:
    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo

    def inyecta_gasolina(self, gasolina):
        self.gasolina = gasolina
