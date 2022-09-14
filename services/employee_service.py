class EmployeeService:
  def __init__(self, employeeRepository):
    self.employeeRepository = employeeRepository

  def createEmployee(self, employee, restaurant_name):
    self.employeeRepository.createEmployee(employee, restaurant_name)

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