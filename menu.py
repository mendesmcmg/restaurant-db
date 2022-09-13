import os
from unicodedata import category
from entities.item import Item
from entities.category import Category
from entities.inventory import Inventory

from services.item_service import ItemService
from services.category_service import CategoryService
from services.inventory_service import InventoryService

class Menu:
  def __init__(self, itemService, categoryService, inventoryService):
    self.itemService = itemService
    self.categoryService = categoryService
    self.inventoryService = inventoryService

  def run(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("------------------------------------------------------------------")
      print("| Seja bem-vindo ao sistema da cadeia de restaurantes Comidinhas |")
      print("------------------------------------------------------------------\n")

      action = int(input("Com o que deseja trabalhar?\n1 - Categoria\n2 - Estoque\n3 - Sair\n"))

      match action:
        case 1:
          self.runCategory()
        case 2:
          self.runInventory()
        case 3:
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

