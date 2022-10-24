class Vehiculo:

#Atributos color, ruedas
    def __init__(self, col, n_ruedas):
        self.color = col
        self.ruedas = n_ruedas

    def __str__(self):
        return "El color del vehículo es {} y el número de ruedas es {}".format(self.color, self.ruedas)

class Coche(Vehiculo):

    def __init__(self, vel, cil, col, n_ruedas):
        super().__init__(col, n_ruedas)
        self.velocidad = vel
        self.cilindrada = cil

    def __str__(self):
        return super().__str__ ()+ "\n" + "La velocidad del vehículo es {} km/h y la cilindrada {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, carga, vel, cil, col, n_ruedas):
        super().__init__(vel, cil, col, n_ruedas)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + "\n" + "La carga del camión es de {} kg".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, tipo, col, n_ruedas):
        super().__init__(col, n_ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + "\n" + "El tipo de bicicleta es {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, vel, cil, tipo, col, n_ruedas):
        super().__init__(tipo, col, n_ruedas)
        self.velocidad = vel
        self.cilindrada= cil

    def __str__(self):
        return super().__str__() + "\n" + "La velocidad de la motocicleta es de {} km/h y la cilindrada es de {}".format(self.velocidad, self.cilindrada)
