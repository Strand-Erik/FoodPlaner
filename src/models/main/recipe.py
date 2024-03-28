from typing import Set, Dict, Any
from src.models.main.ingredient import Ingredient
from src.units.units import *

class Recipe:
    def __init__(self, name: str, toml_map: Dict[str, Any]) -> None:
        self.name = name
        self.ingredients: Set[Ingredient] = self._parse_ingredients(toml_map[name])


    def _parse_ingredients(self, ingredient_data: Dict[str, Any]) -> Set[Ingredient]:
        ingredients = set()
        for item, quantity in ingredient_data.items():
            item = item.lower()  # Ensure the ingredient name is in lowercase
            quantity = quantity.lower()  # Also convert quantity to lowercase to handle units correctly

            # Parse the quantity and unit from the string
            # This simple parsing assumes the format "<quantity> <unit>"
            parts = quantity.split(' ', 1)
            if len(parts) == 2:
                amount, unit_str = parts
                amount = float(amount) if '.' in amount else int(amount)
                unit = get_unit_from_string(unit_str)
                ingredients.add(Ingredient(item, amount, unit))

        return ingredients
    
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Recipe):
            return NotImplemented
        
        return self.name == other.name


    def __hash__(self) -> int:
        return hash(self.name)
