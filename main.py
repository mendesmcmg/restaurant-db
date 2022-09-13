from menu import Menu
from utilities.database_connector import DatabaseConnector

from repositories.item_repository import ItemRepository
from repositories.category_repository import CategoryRepository

from services.item_service import ItemService
from services.category_service import CategoryService

database = DatabaseConnector("restaurant-db")

itemRepository = ItemRepository(database)
categoryRepository = CategoryRepository(database)

itemService = ItemService(itemRepository)
categoryService = CategoryService(categoryRepository)
menu = Menu(itemService, categoryService)

menu.run()

database.disconnect()