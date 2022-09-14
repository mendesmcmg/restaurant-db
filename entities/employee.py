class Employee:
  def __init__(self, name, function, salary, codFunc=None):
    self._name = name
    self._function = function
    self._salary = salary
    self._cod_func = codFunc

  def getName(self):
    return self._name

  def getFunction(self):
    return self._function
  
  def getSalary(self):
    return self._salary

  def setName(self, name):
    self._name = name

  def setFunction(self, function):
    self._function = function

  def setSalary(self, salary):
    self._salary = salary
