from tkinter import *
from PIL import ImageTk, Image
import DataDisplay as dataD
import modelo

def sendData():
    minutes = int(time_entry.get())
    taquillas = int(NumTaquillas.get())
    premiere = int(Premiere.get())
    results = modelo.simular(minutes, taquillas, premiere)
    dataD.showResults(results['taquillas_abiertas'], results['premiere'], results['tiempo_limite'], results['total_personas'], results['infoToSubmit'])
    time_entry.delete(0, END)
    NumTaquillas.set(0)
    Premiere.set(0)


window = Tk()
window.title("Simulación de Cine")
window.geometry('650x300')
window.resizable(False, False)

def only_numbers(char):
    return char.isdigit()
validation = window.register(only_numbers)

# Build UI
time_label = Label(window)
time_label.configure(
    anchor="nw", font="{Cambria} 16 {}", text="Tiempo Límite:", width="100"
)
time_label.place(anchor="nw", relx="0.0", rely="0.10", x="50", y="0")
time_entry = Entry(window, validate="key", validatecommand=(validation, '%S'))
time_entry.configure(
    font="{Cambria} 16 {}", justify="left", state="normal", width="30"
)
time_entry.place(anchor="nw", relx="0.25", rely="0.10", x="50", y="0")
taquillas_label = Label(window)
taquillas_label.configure(
    font="{Cambria} 16 {}", text="Número de taquillas abiertas"
)
taquillas_label.place(anchor="nw", rely="0.25", x="50", y="0")

RadioT_1 = Radiobutton(window)
NumTaquillas = IntVar()
NumTaquillas.set(0)
RadioT_1.configure(text="1", variable=NumTaquillas, value=1)
RadioT_1.place(anchor="nw", rely="0.35", x="50", y="0")
RadioT_2 = Radiobutton(window)
RadioT_2.configure(text="2", variable=NumTaquillas, value=2)
RadioT_2.place(anchor="nw", rely="0.35", x="100", y="0")
RadioT_3 = Radiobutton(window)
RadioT_3.configure(text="3", variable=NumTaquillas, value=3)
RadioT_3.place(anchor="nw", rely="0.35", x="150", y="0")
RadioT_4 = Radiobutton(window)
RadioT_4.configure(text="4", variable=NumTaquillas, value=4)
RadioT_4.place(anchor="nw", rely="0.35", x="200", y="0")
RadioT_5 = Radiobutton(window)
RadioT_5.configure(text="5", variable=NumTaquillas, value=5)
RadioT_5.place(anchor="nw", rely="0.35", x="250", y="0")

SecondsLabel = Label(window)
SecondsLabel.configure(font="{Cambria} 16 {}", text="(m)")
SecondsLabel.place(relx="0.90", rely="0.10", x="0", y="0")

premiere_Label = Label(window)
premiere_Label.configure(
    font="{Cambria} 16 {}", justify="center", text="¿Es estreno?"
)
premiere_Label.place(anchor="nw", rely="0.45", x="50", y="0")

RadioP_1 = Radiobutton(window)
Premiere = IntVar()
Premiere.set(0)
RadioP_1.configure(text="Si", variable=Premiere, value=1)
RadioP_1.place(anchor="nw", rely="0.55", x="50", y="0")
RadioP_2 = Radiobutton(window)
RadioP_2.configure(text="No", variable=Premiere, value=2)
RadioP_2.place(anchor="nw", rely="0.55", x="100", y="0")

img = (Image.open("cinema.png"))
resized_image = img.resize((100, 100), Image.Resampling.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
panel = Label(window, image=new_image)
panel.place(x=0, y=150, relx="0.75", anchor='center')

Submit = Button(window)
Submit.configure(text="Simular", font="{Cambria} 16 {}", command=sendData)
Submit.place(anchor="nw", x="0", y="0", rely="0.80", relx="0.60", width=200, height=25,)

window.mainloop()