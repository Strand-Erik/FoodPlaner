from typing import Dict, Set
from src.models.main.recipe import Recipe

class ListTabModel:
    def __init__(self):
        self.data: Dict[Recipe, int] = {}


    def get_used_recipes(self) -> Set[Recipe]:
        return set(self.data.keys())
