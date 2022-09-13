from menu import Menu
from utilities.database_connector import DatabaseConnector

from repositories.item_repository import ItemRepository
from repositories.category_repository import CategoryRepository
from repositories.inventory_repository import InventoryRepository
from repositories.restaurant_repository import RestaurantRepository

from services.item_service import ItemService
from services.category_service import CategoryService
from services.inventory_service import InventoryService
from services.restaurant_service import RestaurantService

database = DatabaseConnector("restaurant-db")

itemRepository = ItemRepository(database)
categoryRepository = CategoryRepository(database)
inventoryRepository = InventoryRepository(database)
restaurantRepository = RestaurantRepository(database)

itemService = ItemService(itemRepository)
categoryService = CategoryService(categoryRepository)
inventoryService = InventoryService(inventoryRepository)
restaurantService = RestaurantService(restaurantRepository)

menu = Menu(itemService, categoryService, inventoryService, restaurantService)

menu.run()

database.disconnect()