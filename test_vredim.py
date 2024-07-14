from tkinter import ttk
import tkinter as tk
from vn_tk.v_redim import VRedim


class TestVRedim(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        self.vred = VRedim(self, bg='skyblue')
        self.vred.grid(row=0, column=0, sticky="wens")
        self.bind('<Button-3>', self.vred.cerrar)
        self.overrideredirect(1)
        
        #self.config(bg='blue')
        fm = tk.Frame(self, bg='white')
        fm.grid(row=0, column=0, sticky="wens", padx=3, pady=3)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

if __name__=='__main__':
    vn = TestVRedim()
    vn.geometry('400x150')
    vn.title('TestVRedim')
    vn.mainloop()