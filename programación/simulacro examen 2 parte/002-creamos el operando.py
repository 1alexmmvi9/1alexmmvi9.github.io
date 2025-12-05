import tkinter as tk                                                       

ventana = tk.Tk();                                                         

tk.Label(ventana,text="Introduce el primer numero").pack(padx=20,pady=4)
tk.Entry(ventana).pack(padx=20,pady=4)                                    

tk.Label(ventana,text="Introduce el segundo numero").pack(padx=20,pady=4) eta
tk.Entry(ventana).pack(padx=20,pady=4)                                     

ventana.mainloop();
