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

def catalogar(vehiculo):
    for i in vehiculo:
        print (type(i).__name__ + ":" + "\n",i,"\n")

#Añado None porque estoy metiendo un argumento que es opcional
def catalogar_ruedas(lista_vehiculo, ruedas=None):
    contador=0
    for i in lista_vehiculo:
        if ruedas == None:
            print(type(i).__name__+ ":" + "\n",i,"\n")
        else:
            if i.ruedas == ruedas:
                print(type(i).__name__+ ":" + "\n",i,"\n")
                contador +=1
    if ruedas != None:
        print ("Se han encontrado {} vehiculos con {} ruedas".format(contador, ruedas))
        

vehiculo = []        
A = Vehiculo("rojo", 0)
#print(A)
vehiculo.append(A)
B= Coche(100, 50, "azul", 4)
#print("\n",B)
vehiculo.append(B)
C= Camioneta(1000, 200, 60, "negro", 2)
#print("\n",C)
vehiculo.append(C)
D = Bicicleta("urbana", "verde", 4)
#print("\n",D)
vehiculo.append(D)
E = Motocicleta(1000, 10, "deportiva", "rojo", 4)
#print("\n",E)
vehiculo.append(E)
catalogar(vehiculo)
catalogar_ruedas(vehiculo)
catalogar_ruedas(vehiculo, 0)
catalogar_ruedas(vehiculo, 2)
catalogar_ruedas(vehiculo, 4)



