from tkinter import ttk
import tkinter as tk
from vn_tk.v_redim import VRedim
from vn_tk.barra import Barra
from vn_tk.drag_para import DragPara


class VentanaTk(tk.Frame):
    def __init__(self, parent=None, cbd='gray10', cbg='white', *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self.color_borde = cbd
        self.color_bg = cbg
        self._config_VentanaTk()
        
    def _config_VentanaTk(self):
        self.vred = VRedim(self.parent, bg=self.color_borde)
        self.vred.grid(row=0, column=0, sticky="wens")
        self.bind('<Button-3>', self.cerrar)
        #self.overrideredirect(1)
        self.fm = tk.Frame(self.parent, bg=self.color_bg)
        self.fm.grid(row=0, column=0, sticky="wens", padx=3, pady=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # BARRA
        self.bar = Barra(self.fm, bg=self.color_borde)
        self.bar.grid(row=0, column=0, sticky="wen")
        self.bar.asigna_titulo('Test VENTANATK')
        self.fm.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)
        self.bar.bt_x.config(command=self.cerrar)
        # ACTIVANDO DRAG
        self.drag = DragPara(self.parent, self.parent)
        self.bar.bind('<Enter>', self._barra_in)
        self.bar.bind('<Leave>', self.nobind)
        
    def recarga_configs(self):
        self.vred.config(bg=self.color_borde)
        self.fm.config(bg=self.color_bg)
        
    def cerrar(self):
        self.parent.destroy()
        
    def nobind(self, e):
        self.parent.unbind('<Motion>')
        self.parent.unbind('<ButtonPress-1>')
        
    def _barra_in(self, e):
        self.parent.bind('<ButtonPress-1>', self.drag.posicion_relativa)
        self.parent.bind('<ButtonRelease-1>', self.nobind)
        
    #def _barra_out(self, e):
    #    self.parent.unbind()

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = VentanaTk()
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('VentanaTk')
    rz.mainloop()