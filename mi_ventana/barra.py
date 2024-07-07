from tkinter import ttk
import tkinter as tk
# from iconos_mv import MisIconos
from frame_botones import FrameBotones


class Barra(tk.Frame):
    def __init__(self, parent, *args, **kw):
        super(Barra, self).__init__(master=parent, *args, **kw)
        self._widget_Barra()
        
    def _widget_Barra(self):
        # VARIABLES
        self.bg = '#404040'
        self.alto = 12
        self.config(bg=self.bg)
        # VARIABLES
        
        self.ico_pro = tk.PhotoImage(file='icos/T_10p_b.png')
        lb_logo = tk.Label(
            self, image=self.ico_pro, text='PROGRAMA', compound='left',
            font=("Consolas", 8, "bold"),
            bg="#101010", fg="#F0EAD6"
        )
        lb_logo.grid(row=0, column=0, sticky='w')
        lb_logo.bind("<Button-1>", self.accion_logo)

        self.menu = tk.Menu(
            lb_logo, tearoff=False,
            activebackground=self.bg,
            font=("Consolas", 8, "bold")
        )
        self.menu.add_command(label='uno')
        self.menu.add_command(label='dos')
        # lb_logo.add_cascade(label="algo", menu=self.menu)

        # TITULO
        self.tex_titulo = tk.Text(
            self, height=1, padx=6, font=("Arial", 8, "bold"),
            # bg=self.bg, fg="#FFD68B", relief="flat"
            bg='red', fg="#FFD68B", relief="flat"
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
        self.bts_base = FrameBotones(self) 
        self.bts_base.grid(row=0, column=3)
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def accion_logo(self, e):
        # COORDENADAS DE LA VENTANA
        wx, wy = self.winfo_rootx(), self.winfo_rooty()
        print(wx, wy)
        # ancho y alto de label
        lb = e.widget
        lbw, lbh = lb.winfo_width(), lb.winfo_height()
        print(lbw, lbh)
        # coordenadas del menu debajo del label
        x, y = wx, wy+lbh
        self.menu.tk_popup(x, y)

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