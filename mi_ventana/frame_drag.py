from tkinter import ttk
import tkinter as tk


class FrameDrag(tk.Frame):
    def __init__(self, parent=None, disable=None, releasecmd=None, *args, **kw):
        super(FrameDrag, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self.disable = disable
        self.release_cmd = releasecmd
        self._widget_FrameDrag()
        
    def _widget_FrameDrag(self):
        if type(self.disable)=='str':
            self.disable = self.disable.lower()
        self.rz = self.parent.winfo_toplevel()
        self.bind('<Button-3>', self.cerrar)
        self.parent.bind('<Button-1>', self.posicion_relativa)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def cerrar(self, e=None):
        self.parent.destroy()
    
    def posicion_relativa(self, e):
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.rz.geometry().split('+')
        self.ox, self.oy = int(geo[1]), int(geo[2])
        self.rel_x = cx - self.ox
        self.rel_y = cy - self.oy
        self.parent.bind('<Motion>', self.drag_wid)
        self.parent.title(f"x:{cx}, y:{cy} | {self.rel_x}, {self.rel_y}")

    def drag_wid(self, e):
        cx, cy = self.parent.winfo_pointerxy()
        x = cx - self.rel_x
        y = cy - self.rel_y
        if self.disable=='x':
            x = self.ox
        elif self.disable=='y':
            y = self.oy
        self.rz.geometry(f'+{x}+{y}')
        self.parent.title(f"{x}, {y}")

    def drag_unbind(self, e):
        self.parent.unbind('<Motion>')
        if self.release_cmd != None:
            self.release_cmd()
        
    
class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("600x300")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        wg = FrameDrag(self)
        wg.grid(row=0, column=0, sticky="wens")
        

if __name__=="__main__":
    app = Ventana()
    app.mainloop()