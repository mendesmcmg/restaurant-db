from entities.inventory import Inventory

class InventoryRepository:
  def __init__(self, database):
    self.database = database

  def createInventory(self, inventory):
    query = "INSERT INTO estoque (nome) VALUES(%s);"
    self.database.getCursor().execute(query, (inventory.getName(),))
    self.database.commit()

  def addInventoryToRestaurant(self, restaurant_name, inventory_name):
    get_inventory_id = "SELECT codestoque FROM estoque WHERE nome = %s;"
    self.database.getCursor().execute(get_inventory_id, (inventory_name,))
    inventory_id = self.database.getCursor().fetchone()[0]

    get_rest_id = "SELECT codrest FROM restaurante WHERE nome = %s;"
    self.database.getCursor().execute(get_rest_id, (restaurant_name,))
    rest_id = self.database.getCursor().fetchone()[0]

    query = " UPDATE restaurante set estoque_codestoque = %s WHERE codrest = %s;"
    self.database.getCursor().execute(query, (inventory_id,rest_id,))
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
