from entities.restaurant import Restaurant

class RestaurantRepository:
  def __init__(self, database):
    self.database = database

  def createRestaurant(self, restaurant):
    query = "INSERT INTO restaurante (nome, telefone, endereco, foto) VALUES(%s, %s, %s, %s);"
    self.database.getCursor().execute(query, (restaurant.getName(), restaurant.getTelephone(), restaurant.getAddress(), restaurant.getPhoto()))
    self.database.commit()

  def getAllRestaurants(self):
    query = "SELECT * FROM restaurante;"
    self.database.getCursor().execute(query)
    result = self.database.getCursor().fetchall()
    return map(lambda row: Restaurant(row[1], row[2], row[3], row[4]), result)

  def getTelephone(self, name):
    query = "SELECT telefone FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    return self.database.getCursor().fetchone()[0]

  def getAddress(self, name):
    query = "SELECT endereco FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    return self.database.getCursor().fetchone()[0]

  def getCodRest(self, name):
    query = "SELECT codrest FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    return self.database.getCursor().fetchone()[0]

  def updateName(self, newName, name):
    query = "UPDATE restaurante SET nome = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newName, name))
    self.database.commit()

  def updateTelephone(self, newTelephone, name):
    query = "UPDATE restaurante SET telefone = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newTelephone, name))
    self.database.commit()

  def updateAddress(self, newAddress, name):
    query = "UPDATE restaurante SET endereco = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newAddress, name))
    self.database.commit()

  def updatePhoto(self, newPhoto, name):
    query = "UPDATE restaurante SET foto = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newPhoto, name))
    self.database.commit()

  def deleteRestaurant(self, name):
    query = "DELETE FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    self.database.commit()

  def addEmployeeToRestaurant(self, name, employee_name, employee_function, employee_salary):
    get_rest_id = "SELECT codrest FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(get_rest_id, (name,))
    rest_id = self.database.getCursor().fetchone()[0]
    query = "INSERT INTO funcionario (nome, cargo, salario, restaurante_codrest) VALUES(%s, %s, %s, %s);"
    self.database.getCursor().execute(query, (employee_name, employee_function, employee_salary, rest_id))
    self.database.commit()
