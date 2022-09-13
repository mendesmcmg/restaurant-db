class Restaurant:
  def __init__(self, name, telephone, address, photo=None):
    self._name = name
    self._telephone = telephone
    self._address = address
    self._photo = photo

  def getName(self):
    return self._name

  def getTelephone(self):
    return self._telephone

  def getAddress(self):
    return self._address

  def getPhoto(self):
    return self._photo

  def setTelephone(self, telephone):
    self._telephone = telephone

  def setAddress(self, address):
    self._address = address

  def setPhoto(self, photo):
    self._photo = photo

  def setName(self, name):
    self._name = name
