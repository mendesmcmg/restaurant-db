class Category:
  def __init__(self, name, cod_categoria = None):
    self._name = name
    self.cod_categoria = cod_categoria

  def getName(self):
    return self._name

  def getCod(self):
    return self.cod_categoria

  def setName(self, name):
    self._name = name