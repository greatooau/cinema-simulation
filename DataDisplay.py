from distutils.log import info
from tkinter import *

def showResults(taquillas, premiere, tiempoLimite, totalPersonas, infoT):

    if taquillas == 1 or taquillas == 2 or taquillas == 3:
        height = 300
    else:
        height = 500

    windowsize = "650x"+str(height)
    window = Tk()
    window.title("Resultados")
    window.geometry(windowsize)
    window.resizable(False, False)

    if premiere == 1:
        estreno = "Día estreno"
    elif premiere == 2:
        estreno = "Día normal"

    results_label = Label(window)
    results_label.configure(
        anchor="nw", font="{Cambria} 16 {}", text="Resultados"+estreno, width="100"
    )
    results_label.place(anchor="nw", x="50", y="10")

    infoTaquillas = ["Taquilla 1:", "Taquilla 2:", "Taquilla 3:", "Taquilla 4:", "Taquilla 5:"]
    setTaquillas = []
    Res_Taquillas = []

    y = 50
    for x in range(taquillas):
        setTaquillas.append(Label(window))
        setTaquillas[x].configure(
        anchor="nw", font="{Cambria} 14 {}", text=infoTaquillas[x], width="100"
        )
        setTaquillas[x].place(anchor="nw", relx="0.0", x="50", y=y)

        Res_Taquillas.append(Label(window))
        Res_Taquillas[x].configure(
        anchor="nw", font="{Cambria} 14 {}", text="Personas Atendidas: "+str(infoT[x][0])+" | Tiempo Promedio: "+str(infoT[x][1]), width="100"
        )
        Res_Taquillas[x].place(anchor="nw", relx="0.0", x="50", y=y+30)

        y += 70
    print(setTaquillas)

    Tlimite_label = Label(window)
    Tlimite_label.configure(
        anchor="nw", font="{Cambria} 14 {}", text="Tiempo Límite: "+str(tiempoLimite)+"m", width="100"
    )
    Tlimite_label.place(anchor="nw", x="50", y="0", rely="0.90", relx="0.00")

    TPersonas_label = Label(window)
    TPersonas_label.configure(
        anchor="nw", font="{Cambria} 14 {}", text="Total Personas Atendidas: "+str(totalPersonas), width="100"
    )
    TPersonas_label.place(anchor="nw", x="250", y="0", rely="0.90",  relx="0.00")

    window.mainloop()