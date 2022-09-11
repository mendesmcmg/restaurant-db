from entities.item import Item

class ItemRepository:
  def __init__(self, database):
    self.database = database

  def createItem(self, item):
    query = "INSERT INTO item (name, price) VALUES(%s, %s);"
    self.database.getCursor().execute(query, (item.getName(), item.getPrice()))
    self.database.commit()

  def updatePrice(self, name, price):
    query = "UPDATE item SET price = %s WHERE name = %s;"
    self.database.getCursor().execute(query, (price, name))
    self.database.commit()

  def getAllItems(self):
    query = "SELECT * FROM item;"
    self.database.getCursor().execute(query)
    result = self.database.getCursor().fetchall()

    return map(lambda row: Item(row[0], row[1]), result)