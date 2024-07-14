from tkinter import ttk
import tkinter as tk
from vn_tk.frame_botones import FrameBotones
from vn_tk.label_menu import LabelMenu
from vn_tk.barra import Barra


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x300")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        bar = Barra(self)
        bar.grid(row=0, column=0, sticky="wen")
        bar.asigna_titulo('NOMBRE ARCHIVO c:/folder/mi directorio', foreground='pink')
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()