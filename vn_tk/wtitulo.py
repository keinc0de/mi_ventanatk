from tkinter import ttk
import tkinter as tk


class WTitulo(tk.Text):
    def __init__(self, parent=None, bg='#303030', *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.fg = '#E5E5E5'
        self.bg = bg
        self.parent = parent
        self._config_WTitulo()
        
    def _config_WTitulo(self):
        self.config(
            height=1, padx=3,
            font=("Consolas", 8, "bold"),
            bg=self.bg, fg=self.fg,
            relief="flat",
            selectbackground='#202020',
            selectforeground='orange',
            state='disabled',
            cursor='fleur',
        )
        
    def msg(self, texto, tag='tg_title', **kw):
        self.config(state='normal')
        self.insert('end', texto, tag)
        self.tag_config(tag, **kw)
        self.config(state='disabled')
        
        
if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('400x150')
    wg = WTitulo()
    wg.msg('hola como estas', foreground='orange')
    wg.grid(row=0, column=0, sticky='wens')
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('WTitulo')
    rz.mainloop()