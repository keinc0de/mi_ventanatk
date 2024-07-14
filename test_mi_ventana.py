from vn_tk.vn_dnd import  VentanaDD

# class Test
class Test_vdnd(VentanaDD):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def evento_drop(self, e):
        super().evento_drop(e)
        print(e.data)
        print(self.archivos)


if __name__=='__main__':
    tv = Test_vdnd()
    tv.geometry('400x150')
    tv.mainloop()