class InventoryService:
  def __init__(self, inventoryRepository):
    self.inventoryRepository = inventoryRepository

  def createInventory(self, inventory):
    self.inventoryRepository.createInventory(inventory)

  def getAllInventories(self):
    return self.inventoryRepository.getAllInventories()
  
  def updateName(self, newName, name):
    self.inventoryRepository.updateName(newName, name)

  def deleteInventory(self, name):
    self.inventoryRepository.deleteInventory(name)

  def addInventoryToRestaurant(self, restaurant_name, inventory_name):
    self.inventoryRepository.addInventoryToRestaurant(restaurant_name, inventory_name)