import tkinter as tk                #importamos libreria

ventana = tk.Tk();

ventana.mainloop();

tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)


