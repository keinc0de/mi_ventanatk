from tkinter import ttk
import tkinter as tk

class MisIconos():
    def __init__(self):
        self.ruta = "icos"

    def ico(self, clave:str):
        return f"{self.ruta}/{clave}.png"
    
class IconoTk():
    def __init__(self):
        self.NORMAL = None
        self.HOVER = None

    def normal(self, **kw):
        """asigna icono 'data o file'"""
        self.NORMAL = tk.PhotoImage(**kw)

    def hover(self, **kw):
        """asigna icono hover 'data o file'"""
        self.HOVER = tk.PhotoImage(**kw)
    
    def icono_tk(self, **kw):
        """obtiene str icono del tipo 'data' o 'file' retorna un icono tk.photoimage"""
        return tk.PhotoImage(**kw)

    
class Boton(tk.Button):
    def __init__(self, parent=None, bg='#303030', *args, **kw):
        super(Boton, self).__init__(master=parent, bg=bg, *args, **kw)
        self.parent = parent
        self.bg = bg
        self.bg_hover = '#272822'
        self.icono = IconoTk()
        self._mi_cnf_Boton()

    def _mi_cnf_Boton(self):
        cnf1 = {
            # 'bg':'#6E7F80',
            'relief':'flat',
            # 'activebackground':'red'
        }
        self.config(**cnf1)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, e):
        self['bg'] = self.bg_hover
        self.config(image=self.icono.HOVER)
    
    def on_leave(self, e):
        self['bg'] = self.bg
        self.config(image=self.icono.NORMAL)

    def asigna_icono(self, **ico):
        self.icono.normal(**ico)
        self.ico = self.icono.icono_tk(**ico)
        self.config(image=self.ico)

    def asigna_icono_hover(self, **ico):
        self.icono.hover(**ico)


class FrameBotones(tk.Frame):
    def __init__(self, parent, bgh='#272822', bgh_x='#F92672', *args, **kw):
        super(FrameBotones, self).__init__(master=parent, *args, **kw)
        self.bgh = bgh
        self.bgh_x = bgh_x
        self._widget_FrameBotones()
        
    def _widget_FrameBotones(self):
        self.bt_izq = self.crea_boton('icos/izq2n_10.png', 'icos/izq2h_10.png', activebackground='blue')
        self.bt_izq.grid(row=0, column=0, sticky='e')
        self.bt_min = self.crea_boton('icos/minn_10.png', 'icos/minh_10.png', bg=self.bgh)
        self.bt_min.grid(row=0, column=1, sticky='e')
        self.bt_fw = self.crea_boton('icos/f2n_10.png', 'icos/f2h_10.png', bg=self.bgh)
        self.bt_fw.grid(row=0, column=2, sticky='e')
        self.bt_x = self.crea_boton('icos/xn_10.png', 'icos/xh_10.png', bg=self.bgh_x)
        self.bt_x.grid(row=0, column=3, sticky='e')

    def crea_boton(self, ico, icoh, bg=None, **kw):
        bt = Boton(self, **kw)
        bt.asigna_icono(file=ico)
        bt.asigna_icono_hover(file=icoh)
        if bg:
            bt.bg_hover = bg
        return bt

        
    
class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("300x100")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = FrameBotones(self)
        wg.grid(row=0, column=0, sticky="wens")
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()