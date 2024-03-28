from src.models.main.grocery_list import GroceryList
import toml

from src.models.main.recipe import Recipe

file_path = "src/config/recipes.toml"

data = toml.load(file_path)

glist = GroceryList({Recipe("tika masala", data): 13, Recipe("curry", data): 10})

for ing in glist.get_list():
    print(ing)