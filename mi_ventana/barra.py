from tkinter import ttk
import tkinter as tk
# from iconos_mv import MisIconos
from frame_botones import FrameBotones
from label_menu import LabelMenu


class Barra(tk.Frame):
    def __init__(self, parent, bg='#303030', height=12, *args, **kw):
        super(Barra, self).__init__(master=parent, *args, **kw)
        # VARIABLES
        self.bg = bg
        self.alto = height
        # VARIABLES
        self._widget_Barra()
        
    def _widget_Barra(self):
        self.config(bg=self.bg, height=self.alto)
        # ICONO LABEL
        self.lb_menu = LabelMenu(self)
        self.lb_menu.grid(row=0, column=0)

        # TITULO
        self.tex_titulo = tk.Text(
            self, height=1, padx=6, font=("Consolas", 8, "bold"),
            # bg=self.bg, fg="#FFD68B", relief="flat"
            bg='#303030', fg="#E5E5E5", relief="flat",
            selectbackground='#202020',
            selectforeground='orange',
        )
        self.tex_titulo.grid(row=0, column=1)
        self.tex_titulo.insert("end", "TITULO SECUNDARIO FILE: c:/folder/mi_directorio")
        # INFO
        # self.tex_info = tk.Text(
        #     self, height=self.alto, padx=3, font=("Arial", 8, "bold"),
        #     bg="#444335", fg="#F0EAD6", relief="flat",
        #     width=8
        # )
        # self.tex_info.grid(row=0, column=2)
        # self.tex_info.insert("end", "EXt: MP4")
        
        # agregando botones basicos
        self.bts_base = FrameBotones(self, bgh='black')
        self.bts_base.grid(row=0, column=3)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x20")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = Barra(self)
        wg.grid(row=0, column=0, sticky="wens")
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()