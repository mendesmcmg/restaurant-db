from menu import Menu
from repositories.item_repository import ItemRepository
from services.item_service import ItemService
from utilities.database_connector import DatabaseConnector

database = DatabaseConnector("restaurant-db")
itemRepository = ItemRepository(database)
itemService = ItemService(itemRepository)
menu = Menu(itemService)

menu.run()

database.disconnect()