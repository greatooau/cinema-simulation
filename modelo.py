import random

def simular(TLimite:int, numTaqAbiertas:int, premiere:int):
    esEstreno = True if premiere == 1 else False

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
    tiempoTaquilla = []
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
        tiempoTaquilla.append(0)
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
                tiempoTaquilla[i] += delta

    totalPersonasAtendidas = 0
    for i in range(numTaqAbiertas):

        totalPersonasAtendidas += personasAtendidas[i]
        tiempoPromedio.append(tiempoTaquilla[i] / personasAtendidas[i])
        print(f"Tiempo promedio de la caja {i + 1}: {tiempoPromedio[i]}")
        print(f"Personas atendidas en la caja {i + 1}: {personasAtendidas[i]}")
        print("\n")
    print(f"Tiempo simulado en minutos: {TLimite}")
    print(f"Total de personas atendidas: {totalPersonasAtendidas}")

    infoToSubmit = []
    [infoToSubmit.append([personasAtendidas[x], tiempoPromedio[x]]) for x in range(numTaqAbiertas)]
        #"taquillas (1-5), premiere (1-2), tiempoLimite(m), totalPersonas (int), infoToSubmit"
    return {
        "taquillas_abiertas":numTaqAbiertas,
        "premiere":premiere,
        "tiempo_limite":TLimite,
        "total_personas":totalPersonasAtendidas,
        "infoToSubmit":infoToSubmit
    }