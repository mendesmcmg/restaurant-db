from entities.category import Category

class CategoryRepository:
  def __init__(self, database):
    self.database = database

  def createCategory(self, category):
    query = "INSERT INTO categoria (nome) VALUES(%s);"
    self.database.getCursor().execute(query, (category.getName(),))
    self.database.commit()

  def getAllCategories(self):
    query = "SELECT * FROM categoria;"
    self.database.getCursor().execute(query)
    result = self.database.getCursor().fetchall()
    return map(lambda row: Category(row[0], row[1]), result)

  def updateName(self, newName, name):
    query = "UPDATE categoria SET nome = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newName, name))
    self.database.commit()

  def deleteCategory(self, name):
    query = "DELETE FROM categoria WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    self.database.commit()

  def addRestaurantToCategory(self, name, restaurant_name, restaurant_telephone, restaurant_address):
    create_rest = "INSERT INTO restaurante (nome, telefone, endereco) VALUES(%s, %s, %s);"
    self.database.getCursor().execute(create_rest, (restaurant_name, restaurant_telephone, restaurant_address))
    self.database.commit()

    get_rest_id = "SELECT codrest FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(get_rest_id, (restaurant_name,))
    self.database.commit()
    rest_id = self.database.getCursor().fetchone()[0]

    get_category_id = "SELECT codcat FROM categoria WHERE nome = %s;"
    self.database.getCursor().execute(get_category_id, (name,))
    self.database.commit()
    category_id = self.database.getCursor().fetchone()[0]

    create_restaurant_category = "INSERT INTO restaurante_categoria (restaurante_codrest, categoria_codcat) VALUES(%s, %s);"
    self.database.getCursor().execute(create_restaurant_category, (rest_id, category_id))
    self.database.commit()

