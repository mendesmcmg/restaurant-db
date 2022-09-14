class EmployeeService:
  def __init__(self, employeeRepository):
    self.employeeRepository = employeeRepository

  def createEmployee(self, employee):
    self.employeeRepository.createEmployee(employee)

  def getAllEmployees(self):
    return self.employeeRepository.getAllEmployees()
  
  def updateName(self, newName, name):
    self.employeeRepository.updateName(newName, name)

  def updateFunction(self, newFunction, name):
    self.employeeRepository.updateFunction(newFunction, name)

  def updateSalary(self, newSalary, name):
    self.employeeRepository.updateSalary(newSalary, name)

  def deleteEmployee(self, name):
    self.employeeRepository.deleteEmployee(name)