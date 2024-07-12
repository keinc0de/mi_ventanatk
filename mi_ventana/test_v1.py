from tkinter import ttk
import tkinter as tk
from frame_drag import FrameDrag
from barra import Barra


class MiVentana(FrameDrag):
    def __init__(self, parent=None, *args, **kw):
        super(MiVentana, self).__init__(master=parent, *args, **kw)
        self._widget_MiVentana()
        
    def _widget_MiVentana(self):
        pass
        
    
class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("400x300")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = FrameDrag(self)
        wg.grid(row=0, column=0, sticky="wens")
        self.overrideredirect(1)

        bar = Barra(wg)
        bar.grid(row=0, column=0, sticky='wens', padx=2)
        self.columnconfigure(0, weight=1)
        wg.columnconfigure(0, weight=1)
        bar.bts_base.bt_x.config(command=wg.cerrar)
        bg = 'black'
        # wg.grip_ne.config(bg=bg)
        wg.grip_nw.config(bg=bg)
        wg.grip_sw.config(bg=bg)
        # self.attributes('-transparentcolor', 'green')
        bar.tex_titulo.config(state='disabled')

        wtex = tk.Text(wg, bg='skyblue')
        wtex.grid(row=1, column=0, sticky='wens')
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()