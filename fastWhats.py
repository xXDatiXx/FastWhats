import webbrowser
import tkinter as tk
import time
#import pyautogui

# Función para abrir WhatsApp web
def abrirWhatsapp(num, opc):
    if opc == 1:
        webbrowser.open("https://web.whatsapp.com/send?phone=" + num)
        #time.sleep(8)
        #pyautogui.write("Hola de Clean Walkers Naucalpan, tu servicio ya esta listo!")
        #pyautogui.press('enter')
    elif opc == 0:
        webbrowser.open("https://web.whatsapp.com/send?phone=" + num)

#Ventana
ventana = tk.Tk()
ventana.configure(bg='#ffffff')
ventana.title("Fast Whatsapp by Dati")
ventana.geometry("800x300")
ventana.resizable(False,False)

#Label
label = tk.Label(ventana, bg='#ffffff', text="Ingrese el numero de telefono: ", font=("Helvetica", 24))
label.place(x=10, y=10)

#entry para pedir el numero 
num = tk.Entry(ventana, font=("Helvetica", 20))
num.place(x=460, y=15)
entrada = num.get()
        
# Boton para abrir whatsapp
boton = tk.Button(ventana, bg='#3fc150', text="Abrir Whatsapp", font=("Helvetica", 16), width=20, height=2, command=lambda: abrirWhatsapp(num.get(), 0))
boton.place(x=500, y=80)

# Boton para abrir whatsapp y mandar mensaje
boton2 = tk.Button(ventana, bg='#3fc150', text="(Próximamente)", font=("Helvetica", 16), width=20, height=2, command=lambda: abrirWhatsapp(num.get(), 1))
boton2.place(x=500, y=160)

#Imagen
img = tk.PhotoImage(file="LogoCW.png")
labelImg = tk.Label(ventana, bg='#ffffff' , image=img)
labelImg.place(x=10,y=40)

#Activar boton con tecla enter
ventana.bind('<Return>', lambda event:abrirWhatsapp(num.get()))

ventana.mainloop()