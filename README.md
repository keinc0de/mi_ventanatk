# mi ventanatk

## tests
### test_dragpara
se inicializa **DragPara(widget)** se habilita el movimiento con `self.bind('<ButtonPress-1>', self.drag.posicion_relativa)` 
y para detener el movimiento de la ventana una vez se deja de presionar `self.bind('<ButtonRelease-1>', self.nobind)`
siendo **nobind**:

```python
def nobind(self, e):
	self.unbind('<Motion>')
	#self.unbind('<ButtonPress-1>')
```
esto es para desactivar el arrastre, de lo contrario no dejara de mover la ventana

