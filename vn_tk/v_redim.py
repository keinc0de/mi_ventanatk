from tkinter import ttk
import tkinter as tk


class VRedim(tk.Frame):
    def __init__(self, parent=None, bg='black', disable=None,*args, **kw):
        super().__init__(master=parent, bg=bg, *args, **kw)
        self.parent = parent
        self.disable = disable
        self.bg = bg
        self._config_VRedim()
        
    def _config_VRedim(self):
        if type(self.disable)=='str':
                self.disable = self.disable.lower()
        self.rz = self.parent.winfo_toplevel()
        self.bind('<Button-3>', self.cerrar)
        # AGEGANDO LOS GRIPS
        self.grip_se = self.mkGrip(1.0, 1.0, 'se', bg=self.bg)
        self.grip_e = self.mkGrip(1.0, 0.5, 'e', bg=self.bg)
        self.grip_ne = self.mkGrip(1.0, 0, 'ne', bg=self.bg)
        self.grip_nw = self.mkGrip(0, 0, 'nw', bg=self.bg)
        self.grip_w = self.mkGrip(0, 0.5, 'w', bg=self.bg)
        self.grip_sw = self.mkGrip(0, 1.0, 'sw', bg=self.bg)
        
    def cerrar(self, e=None):
        self.parent.destroy()
        
    def mkGrip(self, x, y, anchor:str, **kw):
        grip = tk.Label(self.parent, cursor='sizing', **kw)
        grip.place(relx=x, rely=y, anchor=anchor)
        grip.bind('<B1-Motion>',lambda e,mode=anchor:self._enMovimiento(e,mode))
        return grip
        
    def posicion_relativa(self, e):
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.rz.geometry().split('+')
        self.ox, self.oy = int(geo[1]), int(geo[2])
        self.rel_x = cx - self.ox
        self.rel_y = cy - self.oy
        self.bind('<Motion>', self.drag_wid)

    def drag_wid(self, e):
        cx, cy = self.parent.winfo_pointerxy()
        x = cx - self.rel_x
        y = cy - self.rel_y
        if self.disable=='x':
            x = self.ox
        elif self.disable=='y':
            y = self.oy
        self.rz.geometry(f'+{x}+{y}')
        
    def drag_unbind(self, e):
        self.unbind('<Motion>')
        
    def _enMovimiento(self, e, modo=None):
        self.parent.update()
        x, y = self.parent.winfo_rootx(), self.parent.winfo_rooty()
        abs_x = self.parent.winfo_pointerx()-x
        abs_y = self.parent.winfo_pointery()-y
        w, h = self.parent.winfo_width(), self.parent.winfo_height()
        hmin = 40

        if modo=='se' and abs_x>0 and abs_y>0:
            self._gm_wh(abs_x, abs_y)
        elif modo=='e':
            if h>0 and abs_x>0:
                self._gm_wh(abs_x, h)
        elif modo=='ne' and abs_x>0:
            y+=abs_y
            h-=abs_y
            if h>hmin:
                self._gm(abs_x, h, y, x)
        elif modo=='n':
            h-=abs_y
            y+=abs_y
            if h>0 and w>0:
                self._gm(w, h, x, y)
        elif modo=='nw':
            w-=abs_x
            h-=abs_y
            x+=abs_x
            y+=abs_y
            if h>hmin and w>0:
                self._gm(w,h,x,y)
        elif modo=='w':
            w-=abs_x
            x+=abs_x
            if h>0 and w>0:
                self._gm(w,h,x,y)
        elif modo=='sw':
            w-=abs_x
            h-=(h-abs_y)
            x+=abs_x
            if h>hmin and w>0:
                self._gm(w,h,x,y)
        elif modo=='s':
            h-=(h-abs_y)
            if h>0 and w>0:
                self._gm(w,h,x,y)

    def _gm_wh(self, w, h):
        self.parent.geometry(f'{w}x{h}')

    def _gm(self, w, h, x, y):
        self.parent.geometry(f'{w}x{h}+{x}+{y}')
        

if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = VRedim(rz)
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('VRedim')
    rz.overrideredirect(1)
    rz.mainloop()