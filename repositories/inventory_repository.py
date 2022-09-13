from entities.inventory import Inventory

class InventoryRepository:
  def __init__(self, database):
    self.database = database

  def createInventory(self, inventory):
    query = "INSERT INTO estoque (nome) VALUES(%s);"
    self.database.getCursor().execute(query, (inventory.getName(),))
    self.database.commit()

  def getAllInventories(self):
    query = "SELECT * FROM estoque;"
    self.database.getCursor().execute(query)
    result = self.database.getCursor().fetchall()
    return map(lambda row: Inventory(row[0], row[1]), result)

  def updateName(self, newName, name):
    query = "UPDATE estoque SET nome = %s WHERE nome = %s;"
    self.database.getCursor().execute(query, (newName, name))
    self.database.commit()

  def deleteInventory(self, name):
    query = "DELETE FROM estoque WHERE nome = %s;"
    self.database.getCursor().execute(query, (name,))
    self.database.commit()
