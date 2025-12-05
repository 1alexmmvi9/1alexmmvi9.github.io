import tkinter as tk                                                          

ventana = tk.Tk();                                                            

operando1 = tk.IntVar()                                                     
operando2 = tk.IntVar()                                                         
operacion = tk.StringVar()                                                    

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

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
    elif operacion.get() == "*":
        numeroresultado = multiplicacion(operando1.get(),operando2.get()) 
    elif operacion.get() == "/":
        numeroresultado = division(operando1.get(),operando2.get()) 
    else:
        numeroresultado = "No permitido"

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
