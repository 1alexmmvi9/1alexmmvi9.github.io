import tkinter as tk            

ventana = tk.Tk();

operando1 = tk.IntVar()
operando2 = tk.IntVar()
operacion = tk.StringVar()

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b

def calcula():
    print("Vamos a calcular")
    global operando1
    global operando2
    global operacion
    global resultado

    
    numeroresultado = None
    if operacion.get() == "+":
        numeroresultado = suma(operando1.get(),operando2.get())
    elif operacion.get() == "-":
        numeroresultado = resta(operando1.get(),operando2.get())
        
    resultado.config(text=numeroresultado)

    
tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4)
tk.Entry(ventana,textvariable = operando1).pack(padx=20,pady=4)

tk.Label(ventana,text="Introduce el IRPF").pack(padx=20,pady=4)
tk.Entry(ventana,textvariable = operando2).pack(padx=20,pady=4)

tk.Label(ventana,text="Escoge la operacion que desea realizar").pack(padx=20,pady=4)
tk.Entry(ventana,textvariable = operacion).pack(padx=20,pady=4)

tk.Label(ventana,text="Pulsame para ejecutar").pack(padx=20,pady=4)
tk.Button(ventana,text="Pulsame",command=calcula).pack(padx=20,pady=4)

tk.Label(ventana,text="tu resultado aparecera aqui").pack(padx=20,pady=4)
resultado = tk.Label(ventana,text="X")
resultado.pack(padx=20,pady=4)

ventana.mainloop();
