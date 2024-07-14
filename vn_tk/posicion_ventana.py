import ctypes

class Operaciones:
    def __init__(self, ventana):
        self.ventana = ventana

    def obten_resolusion_pantalla(self):
        md = ctypes.windll.user32
        md.SetProcessDPIAware()
        return md.GetSystemMetrics(0), md.GetSystemMetrics(1)
    
    def mover(self, w, h, ub='no', barras=0, modx=0, mody=0):
        wp, hp = self.obten_resolusion_pantalla()
        if barras!=0:
            hp += barras
        if ub=='no':
            x, y = 0+modx, 0+mody
        elif ub=='ne':
            x, y = (wp-modx)-w, 0+mody
        elif ub=='so':
            x, y = 0+modx, (hp-mody)-h
        elif ub=='se':
            x, y = (wp-modx)-w, (hp-mody)-h
        elif ub=='ctop':
            x, y = wp//2-w//2, 0+mody
        elif ub=='cbot':
            x, y = wp//2-w//2, (hp-mody)-h
        elif ub=='c':
            x, y = wp//2-w//2, hp//2-h//2
        # PARA TKINTER
        self.ventana.geometry(f"+{x}+{y}")
        # PARA QT
        # self.ventana.move(x, y)


class Arriba(Operaciones):
    def __init__(self, ventana, w, h, barras=0, modx=0 ,mody=0):
        super().__init__(ventana=ventana)
        self.dc = {'w':w, 'h':h, 'barras':barras, 'modx':modx, 'mody':mody}

    def izquierda(self):
        self.mover(ub='no', **self.dc)

    def derecha(self):
        self.mover(ub='ne', **self.dc)

    def centrar(self):
        self.mover(ub='ctop', **self.dc)


class Abajo(Arriba):
    def __init__(self, ventana, w, h, barras, modx=0 ,mody=0):
        super().__init__(ventana, w, h, barras, modx ,mody)

    def izquierda(self):
        self.mover(ub='so', **self.dc)

    def derecha(self):
        self.mover(ub='se', **self.dc)

    def centrar(self):
        self.mover(ub='cbot', **self.dc)


class PosicionVentana:
    def __init__(self, ventana, w, h, barras=-60, modx=0, mody=0):
        self.ventana = ventana
        self.d = {
            'w':w, 'h':h,
            'barras':barras,
            'modx':modx, 'mody':mody
        }
        self.arriba = Arriba(ventana=self.ventana, **self.d)
        self.abajo = Abajo(ventana=self.ventana, **self.d)

    def centrar(self):
        coo = Operaciones(self.ventana)
        coo.mover(ub='c', **self.d)

