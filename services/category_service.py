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