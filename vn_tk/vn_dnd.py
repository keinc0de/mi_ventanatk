from tkinter import ttk
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES


class VentanaDD(TkinterDnD.Tk):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.archivos = None
        self.asigna_metodo_a_drop(self.evento_drop)
        
    def asigna_metodo_a_drop(self, metodo):
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', metodo)
        
    def _fix_rutas(self, texto):
        archivos = []
        res = []
        _ = ':'
        inicial = 0
        for x in range(texto.count(_)):
            indice = texto.index(_, inicial, -1)
            res.append(indice-1)
            inicial = indice+1
        res.append(-1)

        inicial = 0
        for indice in res[1:]:
            url = texto[inicial:] if indice==-1 else texto[inicial:indice]
            archivos.append(url.strip('{} '))
            inicial = indice
        return archivos
        
    def evento_drop(self, e):
        self.archivos = self._fix_rutas(e.data)
        

if __name__=='__main__':
    vn = VentanaDD()
    vn.geometry('400x150')
    vn.title('VentanaDD')
    ico64 = '''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAy0lEQVR4nGNkgAINjYL
    /DESCGzcmMMLYjDDNYW7fGUpSrhDU3DNHh2HVLk6GW0+vn/z3eacFIymasRnCxMDAQJJmdPUsDAwMDH/
    +MDFYRRljKDy27CxcHJl9atVpuBombJpIARgGkAoGoQGwgFrY/oiBgYGBYV7LYxRxdMCCLoAcwgwMDAw
    6ai8YTq16wcDAwMBgFmZK2AWkAhYGBgYGFpZ/GDZjA9jUMDEwQJImKQBZPdONGxMYV+3iJNoQjMwEkyA
    lO8M0MzAwMAAAyqBYNbL6eOEAAAAASUVORK5CYII='''
    icono = tk.PhotoImage(data=ico64)
    vn.iconphoto(1, icono)
    vn.mainloop()