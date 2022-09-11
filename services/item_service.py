class ItemService:
  def __init__(self, itemRepostory):
    self.itemRepostory = itemRepostory

  def createItem(self, item):
    self.itemRepostory.createItem(item)

  def updatePrice(self, name, price):
    self.itemRepostory.updatePrice(name, price)

  def getAllItems(self):
    return self.itemRepostory.getAllItems()