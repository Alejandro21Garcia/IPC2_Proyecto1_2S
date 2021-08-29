class terreno:
  def __init__(self, nombre, m, n, xo, yo, xf, yf):
    self.nombre = nombre
    self.m = m
    self.n = n
    self.xo = xo
    self.yo = yo
    self.xf = xf
    self.yf = yf


class nodo:
  def __init__(self, terreno=None, siguiente=None):
    self.terreno = terreno
    self.siguiente = siguiente

class lista_enlazada:
  def __init__(self):
    self.primero = None

  def insertar(self, terreno):
    if self.primero is None:
      self.primero = nodo(terreno=terreno)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(terreno=terreno)

  def recorrer(self):
    actual = self.primero
    while actual != None:
      print("Nombre:", actual.terreno.carne, " Dimensiones \nm: ", actual.terreno.m, "n:",  actual.terreno.n,
            "Xo= ", actual.terreno.xo," Yo= ", actual.terreno.yo, " Xf= ", actual.terreno.xf," Yf= ", actual.terreno.yf,  "->")
      actual = actual.siguiente

  def buscar(self, nombre):
    actual = self.primero

    while actual and actual.terreno.nombre != nombre:
      actual = actual.siguiente

    if actual is None:
      print('El terreno no existe en la lista')
    elif actual:
      print("Nombre:", actual.terreno.nombre, " nombre:", actual.estudiante.nombre, "Dimensiones: m: ", actual.terreno.m, "n:",  actual.terreno.n,
            "Xo= ", actual.terreno.xo," Yo= ", actual.terreno.yo, " Xf= ", actual.terreno.xf, " Yf= ", actual.terreno.yf)