from menu import Menu
from utilities.database_connector import DatabaseConnector

from repositories.item_repository import ItemRepository
from repositories.category_repository import CategoryRepository
from repositories.inventory_repository import InventoryRepository
from repositories.restaurant_repository import RestaurantRepository
from repositories.employee_repository import EmployeeRepository

from services.item_service import ItemService
from services.category_service import CategoryService
from services.inventory_service import InventoryService
from services.restaurant_service import RestaurantService
from services.employee_service import EmployeeService

database = DatabaseConnector("restaurant-db")

itemRepository = ItemRepository(database)
categoryRepository = CategoryRepository(database)
inventoryRepository = InventoryRepository(database)
restaurantRepository = RestaurantRepository(database)
employeeRepository = EmployeeRepository(database)

itemService = ItemService(itemRepository)
categoryService = CategoryService(categoryRepository)
inventoryService = InventoryService(inventoryRepository)
restaurantService = RestaurantService(restaurantRepository)
employeeService = EmployeeService(employeeRepository)

menu = Menu(itemService, categoryService, inventoryService, restaurantService, employeeService)

menu.run()

database.disconnect()