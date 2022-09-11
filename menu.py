import os
from entities.item import Item
from services.item_service import ItemService

class Menu:
  def __init__(self, itemService : ItemService) -> None:
    self.itemService : ItemService = itemService

  def run(self) -> None:
    while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("O que deseja fazer?")
      print("1 - Criar um item")
      print("2 - Ver todos os items")
      print("3 - Atualizar preço")
      print("4 - Sair")
      type = int(input())

      if type == 1:
            self.createItem()
      elif type == 2:
            self.getAllItems()
      elif type == 3:
            self.updatePrice()
      elif type == 4:
            break
  
  def createItem(self) -> None:
    name : str = input("Digite o nome\n")
    price :int = int(input("Digite o preço\n"))
    item : Item = Item(name, price)
    self.itemService.createItem(item)
    input("Item Criado\nAperte ENTER\n")

  def getAllItems(self) -> None:
    items : list[Item] = self.itemService.getAllItems()
    for item in items:
      print("name: {}, price: {}".format(item.getName(), item.getPrice()))
    input("Aperte ENTER\n")

  def updatePrice(self) -> None:
    name : str= input("Digite o nome\n")
    price : int = int(input("Digite o novo preço\n"))
    self.itemService.updatePrice(name, price)
    input("Preco atualizado\nAperte ENTER\n")