class Employee:
  def __init__(self, name, function, salary, codFunc=None, codRest=None):
    self._name = name
    self._function = function
    self._salary = salary
    self._cod_func = codFunc
    self._cod_rest = codRest

  def getName(self):
    return self._name

  def getFunction(self):
    return self._function
  
  def getSalary(self):
    return self._salary

  def getCodFunc(self):
    return self._cod_func

  def getCodRest(self):
    return self._cod_rest

  def setName(self, name):
    self._name = name

  def setFunction(self, function):
    self._function = function

  def setSalary(self, salary):
    self._salary = salary

  def setCodRest(self, codRest):
    self._cod_rest = codRest
