import tkinter as tk                #importamos libreria

ventana = tk.Tk();


tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)

tk.Label(ventana,text="Escoge la operacion que desea realizar").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)

tk.Label(ventana,text="Pulsame para ejecutar").pack(padx=20,pady=4)
tk.Entry(ventana,text="Pulsame").pack(padx=20,pady=4)



ventana.mainloop();
