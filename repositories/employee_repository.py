from entities.employee import Employee

class EmployeeRepository:
  def __init__(self, database):
    self.database = database

  def createEmployee(self, employee):
    query = "INSERT INTO funcionario (nome, cargo, salario) VALUES(%s, %s, %s);"
    self.database.getCursor().execute(query, (employee.getName(), employee.getFunction(), employee.getSalary(),))
    self.database.commit()

  def getAllEmployees(self):
    query = "SELECT * FROM funcionario;"
    self.database.getCursor().execute(query)
    result = self.database.getCursor().fetchall()
    return map(lambda row: Employee(row[2], row[1], row[3]), result)

  def getCodFunc(self, name):
    query = "SELECT codfunc FROM funcionario WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    return self.database.getCursor().fetchone()[0]

  def getCodRest(self, name):
    query = "SELECT restaurante_codrest FROM funcionario WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    return self.database.getCursor().fetchone()[0]

  def updateName(self, newName, name):
    query = "UPDATE funcionario SET nome = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newName, name))
    self.database.commit()

  def updateFunction(self, newFunction, name):
    query = "UPDATE funcionario SET cargo = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newFunction, name))
    self.database.commit()

  def updateSalary(self, newSalary, name):
    query = "UPDATE funcionario SET salario = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newSalary, name))
    self.database.commit()

  def deleteEmployee(self, name):
    query = "DELETE FROM funcionario WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    self.database.commit()
