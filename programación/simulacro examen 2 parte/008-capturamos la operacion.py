import tkinter as tk                                                      

ventana = tk.Tk();                                                        

operando1 = tk.IntVar()                                                 
operando2 = tk.IntVar()                                                 
operacion = tk.StringVar()                                             

def calcula():
    print("Vamos a calcular algo")
    global operando1                                                    
    global operando2
    global operacion
    global resultado
    print(operando1.get())
    numeroresultado = None
    if operacion.get() == "+":
        print("suma")
        numeroresultado = operando1.get()+operando2.get()
        resultado.config(text=numeroresultado)
        

tk.Label(ventana,text="Introduce el primer operando").pack(padx=20,pady=4) 
tk.Entry(ventana,textvariable = operando1).pack(padx=20,pady=4)                                     

tk.Label(ventana,text="Introduce el segundo operando").pack(padx=20,pady=4) 
tk.Entry(ventana,textvariable = operando2).pack(padx=20,pady=4)                                      

tk.Label(ventana,text="Escoge operación").pack(padx=20,pady=4)             
tk.Entry(ventana,textvariable = operacion).pack(padx=20,pady=4)                                    

tk.Label(ventana,text="Pulsa para ejecutar").pack(padx=20,pady=4)              
tk.Button(ventana,text="Vamos alla!",command=calcula).pack(padx=20,pady=4)               

tk.Label(ventana,text="El resultado aparecerá aquí").pack(padx=20,pady=4) 
resultado = tk.Label(ventana,text="X")
resultado.pack(padx=20,pady=4)

ventana.mainloop();
