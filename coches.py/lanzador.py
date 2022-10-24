from clases import Vehiculo, Coche, Camioneta, Motocicleta, Bicicleta

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
        
def solucion():
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



