import tkinter as tk                #importamos libreria

ventana = tk.Tk();

operando1 = tk.IntVar()
operando2 = tk.IntVar()
operando3 = tk.IntVar()
operacion = tk.StringVar()

def calcula():
    print("Vamos a calcular")
    global operando1
    global operando2
    global operando3
    global operacion
    global resultado
    print(operando1.get())
    numeroresultado = None
    if operacion.get() =="%":
        print("procentaje")
        numeroresultado = operando1.get()-operando2.get()+operando3.get()
        resultado.config(text=numeroresultado)
    


tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)

tk.Label(ventana,text="Introduce el IRPF").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)

tk.Label(ventana,text="Introduce la el IVA").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)

tk.Label(ventana,text="Escoge la operacion que desea realizar").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)

tk.Label(ventana,text="Pulsame para ejecutar").pack(padx=20,pady=4)
tk.Button(ventana,text="Pulsame").pack(padx=20,pady=4)

tk.Label(ventana,text="tu resultado aparecera aqui").pack(padx=20,pady=4)
resultado = tk.Label(ventana,text="X")
resultado.pack(padx=20,pady=4)

ventana.mainloop();
