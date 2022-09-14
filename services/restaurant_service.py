class RestaurantService:
  def __init__(self, restaurant_repository):
      self.restaurant_repository = restaurant_repository
  
  def createRestaurant(self, restaurant):
      self.restaurant_repository.createRestaurant(restaurant)

  def getAllRestaurants(self):
      return self.restaurant_repository.getAllRestaurants()

  def getCodRest(self, name):
      return self.restaurant_repository.getCodRest(name)

  def updateName(self, newName, name):
      self.restaurant_repository.updateName(newName, name)

  def updateTelephone(self, newTelephone, telephone):
      self.restaurant_repository.updateTelephone(newTelephone, telephone)

  def updateAddress(self, newAddress, address):
      self.restaurant_repository.updateAddress(newAddress, address)

  def updatePhoto(self, newPhoto, photo):
      self.restaurant_repository.updatePhoto(newPhoto, photo)

  def deleteRestaurant(self, name):
      self.restaurant_repository.deleteRestaurant(name)

  def addEmployeeToRestaurant(self, name, employee_name, employee_function, employee_salary):
      self.restaurant_repository.addEmployeeToRestaurant(name, employee_name, employee_function, employee_salary)


