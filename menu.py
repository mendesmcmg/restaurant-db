import os
from entities.category import Category
from entities.inventory import Inventory
from entities.restaurant import Restaurant
from entities.employee import Employee
class Menu:
  def __init__(self, itemService, categoryService, inventoryService, restaurantService, employeeService):
    self.itemService = itemService
    self.categoryService = categoryService
    self.inventoryService = inventoryService
    self.restaurantService = restaurantService
    self.employeeService = employeeService

  def run(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("------------------------------------------------------------------")
      print("| Seja bem-vindo ao sistema da cadeia de restaurantes Comidinhas |")
      print("------------------------------------------------------------------\n")

      action = int(input("Com o que deseja trabalhar?\n1 - Categoria\n2 - Estoque\n3 - Restaurante \n4 - Funcionário\n5 - Sair\n"))

      match action:
        case 1:
          self.runCategory()
        case 2:
          self.runInventory()
        case 3:
          self.runRestaurant()
        case 4:
          self.runEmployee()
        case 5:
          break

  def runCategory(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("------------------------------------------------------------------")
      print("| Seja bem-vindo ao sistema da cadeia de restaurantes Comidinhas |")
      print("------------------------------------------------------------------\n")

      print("CATEGORIA")
      print("O que deseja fazer?")
      print("1 - Criar uma categoria de restaurante")
      print("2 - Ver todas as categorias de restaurantes")
      print("3 - Atualizar categoria de restaurante")
      print("4 - Deletar uma categoria de restaurante")
      print("5 - Sair")
      category = int(input())

      match category:
        case 1:
          self.createCategory()
          self.indexCategory()
        case 2:
          self.indexCategory()
        case 3:
          self.updateName()
          self.indexCategory()
        case 4:
          self.deleteCategory()
          self.indexCategory()
        case 5:
          break
  
  def createCategory(self):
    name = input("Digite o nome da categoria\n")
    category = Category(name)
    self.categoryService.createCategory(category)
    input("Categoria Criada\nAperte ENTER\n")

  def indexCategory(self):
    categories = self.categoryService.getAllCategories()
    for category in categories:
      print("nome: {} \ncódigo: {} \n -----------".format(category.getCod(), category.getName()))
    input("Aperte ENTER\n")

  def updateName(self):
    name = input("Digite o nome original\n")
    new_name = input("Digite o novo nome\n")
    self.categoryService.updateName(new_name, name)
    input("Nome atualizado\nAperte ENTER\n")

  def deleteCategory(self):
    name = input("Digite o nome\n")
    self.categoryService.deleteCategory(name)
    input("Categoria deletada\nAperte ENTER\n")
    

  def runInventory(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("------------------------------------------------------------------")
      print("| Seja bem-vindo ao sistema da cadeia de restaurantes Comidinhas |")
      print("------------------------------------------------------------------\n")

      print("ESTOQUE")
      print("O que deseja fazer?")
      print("1 - Criar um estoque")
      print("2 - Ver todos os estoques")
      print("3 - Atualizar estoque")
      print("4 - Deletar um estoque")
      print("5 - Sair")
      inventory = int(input())

      match inventory:
        case 1:
          self.createInventory()
          self.indexInventory()
        case 2:
          self.indexInventory()
        case 3:
          self.updateName()
          self.indexInventory()
        case 4:
          self.deleteInventory()
          self.indexInventory()
        case 5:
          break

  def createInventory(self):
    name = input("Digite o nome do estoque\n")
    inventory = Inventory(name)
    self.inventoryService.createInventory(inventory)
    input("Estoque Criado\nAperte ENTER\n")

  def indexInventory(self):
    inventories = self.inventoryService.getAllInventories()
    for inventory in inventories:
      print("nome: {} \ncódigo: {} \n -----------".format(inventory.getCodEstoque(), inventory.getName()))
    input("Aperte ENTER\n")

  def updateName(self):
    name = input("Digite o nome original\n")
    new_name = input("Digite o novo nome\n")
    self.inventoryService.updateName(new_name, name)
    input("Nome atualizado\nAperte ENTER\n")

  def deleteInventory(self):
    name = input("Digite o nome\n")
    self.inventoryService.deleteInventory(name)
    input("Estoque deletado\nAperte ENTER\n")

  def runRestaurant(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("RESTAURANTE")
      print("O que deseja fazer?")
      print("1 - Criar um restaurante")
      print("2 - Ver todos os restaurantes")
      print("3 - Atualizar restaurante")
      print("4 - Deletar um restaurante")
      print("5 - Sair")
      restaurant = int(input())

      match restaurant:
        case 1:
          self.createRestaurant()
          self.indexRestaurant()
        case 2:
          self.indexRestaurant()
        case 3:
          self.updateName()
          self.indexRestaurant()
        case 4:
          self.deleteRestaurant()
          self.indexRestaurant()
        case 5:
          break

  def createRestaurant(self):
    name = input("Digite o nome do restaurante\n")
    telephone = input("Digite o telefone do restaurante\n")
    address = input("Digite o endereço do restaurante\n")
    restaurant = Restaurant(name, telephone, address)
    self.restaurantService.createRestaurant(restaurant)
    input("Restaurante Criado\nAperte ENTER\n")

  def indexRestaurant(self):
    restaurants = self.restaurantService.getAllRestaurants()
    for restaurant in restaurants:
      print("nome: {} \ntelefone: {} \nendereço: {} \n------------".format(restaurant.getName(), restaurant.getTelephone(), restaurant.getAddress()))
    input("Aperte ENTER\n")

  def updateName(self):
    name = input("Digite o nome original\n")
    new_name = input("Digite o novo nome\n")
    self.restaurantService.updateName(new_name, name)
    input("Nome atualizado\nAperte ENTER\n")

  def updateTelephone(self):
    name = input("Digite o nome do restaurante\n")
    telephone = input("Digite o novo telefone\n")
    self.restaurantService.updateTelephone(telephone, name)
    input("Telefone atualizado\nAperte ENTER\n")

  def updateAddress(self):
    name = input("Digite o nome do restaurante\n")
    address = input("Digite o novo endereço\n")
    self.restaurantService.updateAddress(address, name)
    input("Endereço atualizado\nAperte ENTER\n")

  def deleteRestaurant(self):
    name = input("Digite o nome\n")
    self.restaurantService.deleteRestaurant(name)
    input("Restaurante deletado\nAperte ENTER\n")

  def runEmployee(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("FUNCIONÁRIO")
      print("O que deseja fazer?")
      print("1 - Criar um funcionário")
      print("2 - Ver todos os funcionários")
      print("3 - Atualizar funcionário")
      print("4 - Deletar um funcionário")
      print("5 - Sair")
      employee = int(input())

      match employee:
        case 1:
          self.createEmployee()
          self.indexEmployee()
        case 2:
          self.indexEmployee()
        case 3:
          self.updateEmployee()
          self.indexEmployee()
        case 4:
          self.deleteEmployee()
          self.indexEmployee()
        case 5:
          break

  def createEmployee(self):
    name = input("Digite o nome do funcionário\n")
    function = input("Digite o cargo do funcionário\n")
    salary = input("Digite o salário do funcionário\n")
    employee = Employee(name, function, salary)
    self.employeeService.createEmployee(employee)
    input("Funcionário Criado\nAperte ENTER\n")

  def indexEmployee(self):
    employees = self.employeeService.getAllEmployees()
    for employee in employees:
      print("nome: {} \ncargo: {} \nsalário: {} \n------------".format(employee.getName(), employee.getFunction(), employee.getSalary()))
    input("Aperte ENTER\n")

  def updateEmployee(self):
    field_to_update = int(input("O que deseja atualizar?\n1 - Nome\n2 - Cargo\n3 - Salário\n"))
    name = input("Digite o nome do funcionário\n")
    match field_to_update:
      case 1:
        new_name = input("Digite o novo nome\n")
        self.employeeService.updateName(new_name, name)
        input("Nome atualizado\nAperte ENTER\n")
      case 2:
        new_role = input("Digite o novo cargo\n")
        self.employeeService.updateFunction(new_role, name)
        input("Cargo atualizado\nAperte ENTER\n")
      case 3:
        new_salary = input("Digite o novo salário\n")
        self.employeeService.updateSalary(new_salary, name)
        input("Salário atualizado\nAperte ENTER\n")

  def deleteEmployee(self):
    name = input("Digite o nome\n")
    self.employeeService.deleteEmployee(name)
    input("Funcionário deletado\nAperte ENTER\n")



