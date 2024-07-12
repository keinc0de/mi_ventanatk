from tkinter import ttk
import tkinter as tk
from frame_botones import FrameBotones
from label_menu import LabelMenu
from posicion_ventana import PosicionVentana
from drag_para import DragPara
from frame_drag import FrameDrag


class Barra(tk.Frame):
    def __init__(self, parent, bg='#303030', height=6, *args, **kw):
        super(Barra, self).__init__(master=parent, *args, **kw)
        self.parent = parent
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
            bg='#303030', fg="#E5E5E5", relief="flat",
            selectbackground='#202020',
            selectforeground='orange',
        )
        self.tex_titulo.grid(row=0, column=1)
        self.tex_titulo.insert("end", "TITULO SECUNDARIO FILE: c:/folder/mi_directorio")
        self.tex_titulo.config(state='disabled')
        
        # agregando botones basicos
        self.bts_base = FrameBotones(self, bgh='black')
        self.bts_base.grid(row=0, column=3)
        # self.fm_ne = tk.Frame(self, bg='red', width=3)
        # self.fm_ne.grid(row=0, column=4, sticky='wens')
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        # comandos
        self.bts_base.bt_x.config(command=self.cerrar)
        self.parent.bind('<Button-2>', self.cerrar)

        # CENTRAR VENTANA
        self.pv = PosicionVentana(self.parent, 600, 16)
        self.pv.centrar()

        # DRAG
        # self.drag = DragPara(self)
        

    def cerrar(self, e=None):
        self.parent.destroy()


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x160")
        
        self.bar = Barra(self)
        self.bar.grid(row=0, column=0, sticky="wens")
        
        # fm = FrameDrag(self, bg='white')
        fm = tk.Text(self, bg='skyblue')
        fm.grid(row=1, column=0, sticky='wens')
        self.overrideredirect(1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.drag = DragPara(self)

    #     self.grip = ttk.Sizegrip(self)
    #     self.grip.place(relx=1.0, rely=1.0, anchor='se')
    #     self.grip.bind("<B1-Motion>", self.onmotion)

    # def onmotion(self, event):
    #     """ function to change window size """
    #     self.wm_state('normal')
    #     # self.maximize.config(text=u"\U0001F5D6")
    #     x1 = self.winfo_pointerx()
    #     y1 = self.winfo_pointery()
    #     x0 = self.winfo_rootx()
    #     y0 = self.winfo_rooty()
    #     self.geometry("%sx%s" % ((x1-x0), (y1-y0)))
    #     return

        self.bar.bind('<Enter>', self.barra_in)
        self.bar.bind('<Leave>', self.barra_out)
        # self.wg.bind('<ButtonPress-1>', self.posicion_relativa)
        # self.wg.bind('<ButtonRelease-1>', self.drag_unbind)

    def barra_in(self, e):
        print("encima")
        self.bind('<ButtonPress-1>', self.drag.posicion_relativa)
        # self.bind('<ButtonRelease-1>', self.drag.drag_unbind)
        self.bind('<ButtonRelease-1>', self.nobind)

    def barra_out(self, e):
        print("fuera")
        self.unbind('<Motion>')

    def nobind(self, e):
        self.unbind('<Motion>')
        self.unbind('<ButtonPress-1>')

if __name__=="__main__":
    app = Ventana()
    app.mainloop()