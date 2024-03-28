from typing import Dict, List
from src.models.main.recipe import Ingredient
from src.models.main.recipe import Recipe

class GroceryList:
    def __init__(self, recipeList: Dict[Recipe, int] = {}) -> None:
        self.glist: Dict[str, Ingredient] = {}
        self.create_ingredient_list(recipeList)
        
    def get_list(self) -> List[Ingredient]:
        return list(self.glist.values())


    def create_ingredient_list(self, recipeList: Dict[Recipe, int]) -> None:
        for recipe, count in recipeList.items():
            self.add_recipe(recipe, count)


    def add_recipe(self, recipe: Recipe, count: int = 1) -> None:
        for ingredient in recipe.ingredients:
            
            ingredient.quantity *= count
            ingredient.normalize_units()
            
            if ingredient.name in self.glist:
                self.glist[ingredient.name] += ingredient
            else:  
                self.glist[ingredient.name] = ingredient


    def subtract_recipe(self, recipe: Recipe, count: int = 1) -> None:
        for ingredient in recipe.ingredients:
            if not ingredient.name in self.glist: continue
            subtractor = Ingredient(ingredient.name, ingredient.quantity*count, ingredient.unit)
            self.glist[ingredient.name] -= subtractor
            
            if self.glist[ingredient.name] == 0:
                self.glist.pop(ingredient.name)