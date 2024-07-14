from tkinter import ttk
import tkinter as tk
from vn_tk.ventanatk import VentanaTk


class TestVentanaTk(tk.Frame):
    def __init__(self, parent=None, *args, **kw):
        super(TestVentanaTk, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self._widget_TestVentanaTk()

    def _widget_TestVentanaTk(self):
        self.vred = VentanaTk(self.parent, cbd='#2D303D', cbg='#808080')
        self.vred.grid(row=0, column=0, sticky="wens")


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x300")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.bind('<Button-3>', self.cerrar)
        self.overrideredirect(1)

        wg = TestVentanaTk(self)
        wg.grid(row=0, column=0, sticky="wens")
        #self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        self.attributes('-topmost', True)

    def cerrar(self, e=None):
        self.destroy()

if __name__=="__main__":
    app = Ventana()
    app.mainloop()