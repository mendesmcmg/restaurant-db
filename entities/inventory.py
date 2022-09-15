class Inventory:
  def __init__(self, name, codEstoque=None):
    self._name = name
    self._cod_estoque = codEstoque

  def getName(self):
    return self._name

  def getCodEstoque(self):
    return self._cod_estoque

  def setName(self, name):
    self._name = name