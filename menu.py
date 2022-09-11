import os
from entities.item import Item
from services.item_service import ItemService

class Menu:
  def __init__(self, itemService):
    self.itemService = itemService

  def run(self):
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("------------------------------------------------------------------")
      print("| Seja bem-vindo ao sistema da cadeia de restaurantes Comidinhas |")
      print("------------------------------------------------------------------\n")

      print("O que deseja fazer?")
      print("1 - Criar uma categoria de restaurante")
      print("2 - Ver todas as categorias de restaurantes")
      print("3 - Atualizar categoria de restaurante")
      print("4 - Deletar uma categoria de restaurante")
      print("5 - Sair")
      type = int(input())

      match type:
        case 1:
          self.create()
          self.index()
        case 2:
          self.index()
        case 3:
          self.updatePrice()
          self.index()
        case 4:
          self.delete()
          self.index()
        case 5:
          break
  
  def create(self):
    name = input("Digite o nome\n")
    price = int(input("Digite o preço\n"))
    item = Item(name, price)
    self.itemService.createItem(item)
    input("Item Criado\nAperte ENTER\n")

  def index(self):
    items = self.itemService.getAllItems()
    for item in items:
      print("name: {}, price: {}".format(item.getName(), item.getPrice()))
    input("Aperte ENTER\n")

  def updatePrice(self):
    name = input("Digite o nome\n")
    price = int(input("Digite o novo preço\n"))
    self.itemService.updatePrice(name, price)
    input("Preco atualizado\nAperte ENTER\n")

  def delete(self):
    name = input("Digite o nome\n")
    self.itemService.deleteItem(name)
    input("Item deletado\nAperte ENTER\n")