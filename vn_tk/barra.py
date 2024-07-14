from tkinter import ttk
import tkinter as tk
from vn_tk.frame_botones import FrameBotones
from vn_tk.label_menu import LabelMenu
from vn_tk.wtitulo import WTitulo


class Barra(tk.Frame):
	def __init__(self, parent=None, bg='#303030',*args, **kw):
		super(Barra, self).__init__(master=parent, bg=bg, *args, **kw)
		# VARIABLES
		self.bg = bg
		self.alto = 12
		self.parent = parent
		self._widget_Barra()
		
	def _widget_Barra(self):
		self.config(bg=self.bg, height=self.alto)
		# ICONO LABEL Y MENU
		self.lb_menu = LabelMenu(self, bg=self.bg)
		self.lb_menu.grid(row=0, column=0)
		
		# TITULO
		self.wg_titulo = WTitulo(self, bg=self.bg)
		self.wg_titulo.grid(row=0, column=1, sticky="wens")
		# BOTONES BASE
		self.bts_base = FrameBotones(self, bgh='black', bg=self.bg)
		self.bts_base.grid(row=0, column=2, sticky='e')
		self.bts_base.bt_x.config(command=self.cerrar)
		# ALINEACION
		self.rowconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		# ACCEDER A BOTONES
		self.bt_x = self.bts_base.bt_x
		
	def asigna_titulo(self, texto, tag='tg_tt', **kw):
		self.wg_titulo.msg(texto, tag, **kw)
		
	def cerrar(self, e=None):
		self.parent.destroy()