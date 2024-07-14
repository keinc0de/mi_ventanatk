from tkinter import ttk
import tkinter as tk
from vn_tk.drag_para import DragPara


class Ventana(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        self.drag = DragPara(self)
        self.bind('<ButtonPress-1>', self.drag.posicion_relativa)
        self.bind('<ButtonRelease-1>', self.nobind)
        self.bind('<Button-3>', self.cerrar)

    def cerrar(self, e=None):
            self.parent.destroy()
        
    def nobind(self, e):
        self.unbind('<Motion>')
        #self.unbind('<ButtonPress-1>')
        

if __name__=='__main__':
    vn = Ventana()
    vn.geometry('400x150')
    vn.title('Ventana')
    vn.mainloop()