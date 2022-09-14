class CategoryService:
  def __init__(self, categoryRepository):
    self.categoryRepository = categoryRepository

  def createCategory(self, category):
    self.categoryRepository.createCategory(category)

  def getAllCategories(self):
    return self.categoryRepository.getAllCategories()
  
  def updateName(self, newName, name):
    self.categoryRepository.updateName(newName, name)

  def deleteCategory(self, name):
    self.categoryRepository.deleteCategory(name)

  def addRestaurantToCategory(self, name, restaurant_name, restaurant_telephone, restaurant_address):
    self.categoryRepository.addRestaurantToCategory(name, restaurant_name, restaurant_telephone, restaurant_address)

  def showRestaurantsFromCategory(self, name):
    return self.categoryRepository.showRestaurantsFromCategory(name)