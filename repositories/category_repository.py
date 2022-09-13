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
