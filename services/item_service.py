class ItemService:
  def __init__(self, itemRepository):
    self.itemRepository = itemRepository

  def createItem(self, item):
    self.itemRepository.createItem(item)

  def getAllItems(self):
    return self.itemRepository.getAllItems()

  def updatePrice(self, name, price):
    self.itemRepository.updatePrice(name, price)

  def deleteItem(self, name):
    self.itemRepository.deleteItem(name)