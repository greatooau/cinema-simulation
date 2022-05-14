import random

def simular(TLimite, numTaqAbiertas, premiere):
    esEstreno = False
    while True:
        try:
            TLimite = int(input("Ingrese el tiempo Limite de la simulación en minutos: "))
        except:
            print("\n\nIngrese un número entero.\n")

        if  TLimite > 0:
            break
        else: 
            print("\nIngrese un número mayor a 0\n.")

    while True:
        try:
            numTaqAbiertas = int(input("\nIngrese el número de taquillas que se abrirán: "))
        except:
            print("\n\nIngrese un número entero.\n")

        if  numTaqAbiertas > 0 and numTaqAbiertas <= 5:
            break
        else: 
            print("\n\nIngrese un número que sea mayor a 0 y menor a 6.\n")

    while True:
        _input = input("¿La simulación será de un estreno? [ Si / No ]\n")

        flag = False

        for letter in _input:
            if letter.isdigit():
                flag = True

        if  _input.lower() == "si" and not flag:
            esEstreno = True
            break
        elif _input.lower() == "no" and not flag:
            break
        else: 
            print("\n\nIngrese una de las opciones.\n")

    def generarVariableAleatoria(media, desv):
        sumR = 0
        for i in range(12):
            R = random.random()
            sumR += R
        X = media + (desv * (sumR - 6))
        return X

    tiempoAtencion = []
    tiempoPromedio = []
    taquillaLibre = []
    tiempoCaja = []
    personasAtendidas = []

    if esEstreno:
        desv = 0.9273
        media = 1.4392
    else:
        desv = 0.8923
        media = 2.4841

        
    for i in range(numTaqAbiertas):
        tiempoAtencion.append(generarVariableAleatoria(media, desv))
        taquillaLibre.append(False)
        tiempoCaja.append(0)
        personasAtendidas.append(0)

    tiempoSimulacion = 0
    delta = 0
    while tiempoSimulacion < TLimite:
        for i in range(numTaqAbiertas):
            if taquillaLibre[i]:
                taquillaLibre[i] = False
                tiempoAtencion[i] = generarVariableAleatoria(media, desv)
        
        delta = min(tiempoAtencion)

        for i in range(numTaqAbiertas):
            tiempoAtencion[i] -= delta
            if tiempoAtencion[i] == 0:
                personasAtendidas[i] += 1
                tiempoSimulacion += delta
                taquillaLibre[i] = True
                tiempoCaja[i] += delta

    totalPersonasAtendidas = 0
    for i in range(numTaqAbiertas):

        totalPersonasAtendidas += personasAtendidas[i]
        tiempoPromedio.append(tiempoCaja[i] / personasAtendidas[i])
        print(f"Tiempo promedio de la caja {i + 1}: {tiempoPromedio[i]}")
        print(f"Personas atendidas en la caja {i + 1}: {personasAtendidas[i]}")
        print("\n")
    print(f"Tiempo simulado en minutos: {TLimite}")
    print(f"Total de personas atendidas: {totalPersonasAtendidas}")

    infoToSubmit = []
    [infoToSubmit.append([personasAtendidas[x], tiempoPromedio[x]]) for x in range(numTaqAbiertas)]

    return "taquillas (1-5), premiere (1-2), tiempoLimite(m), totalPersonas (int), infoToSubmit"