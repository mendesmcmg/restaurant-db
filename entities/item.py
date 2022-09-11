class Item:
  def __init__(self, name, price):
    self._name = name
    self._price = price

  def getName(self):
    return self._name

  def getPrice(self):
    return self._price

  def setName(self, name):
    self._name = name

  def setPrice(self, price):
    self._price = price