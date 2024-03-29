from src.units.main.units import *

class Ingredient:
    def __init__(self, name: str, quantity: float, unit: Enum):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.normalize_units()
        

    def __add__(self, other):
        if not isinstance(other, Ingredient):
            raise ValueError("Can only add an instance of class Ingredient to another Ingredient")
        if self.name != other.name or type(self.unit) != type(other.unit):
            raise ValueError("Ingredients must have the same name and compatible units to be added")

        # Convert both measurements to the base unit before adding
        base_measurement_self: float = self.quantity * self.unit.value
        base_measurement_other: float = other.quantity * other.unit.value
        new_measurement: float = base_measurement_self + base_measurement_other
        
        return Ingredient(self.name, new_measurement, get_base_unit(self.unit))
    
    
    def __sub__(self, other):
        if not isinstance(other, Ingredient):
            raise ValueError("Can only sutract an instance of class Ingredient to another Ingredient")
        if self.name != other.name or type(self.unit) != type(other.unit):
            raise ValueError("Ingredients must have the same name and compatible units to be subtracted")

        # Convert both measurements to the base unit before subtracting
        base_measurement_self: float = self.quantity * self.unit.value
        base_measurement_other: float = other.quantity * other.unit.value
        new_measurement: float = base_measurement_self - base_measurement_other

        # Prevent negative quantities
        if new_measurement < 0:
            new_measurement = 0

        return Ingredient(self.name, new_measurement, get_base_unit(self.unit))
    
    
    def normalize_units(self) -> None:
        self.quantity *= self.unit.value  # Convert to base unit value
        self.unit = get_base_unit(self.unit)
        closest_unit: Enum = self.unit
        min_difference: float = float('inf')
        
        for unit in type(self.unit): # Itterate the diffrent units for our unit type
            if self.quantity >= unit.value and (self.quantity / unit.value) < min_difference:
                closest_unit = unit
                min_difference = self.quantity / unit.value

        self.quantity /= closest_unit.value
        self.unit = closest_unit


    def __repr__(self) -> str:
        # Check if quantity is an integer by comparing it to its rounded version
        if self.quantity == round(self.quantity, 1):
            # If it's effectively an integer, format without decimal part
            formatted_quantity: str = f"{int(self.quantity)}"
        else:
            # Otherwise, format with one decimal place
            formatted_quantity: str = f"{self.quantity:.1f}"
        
        return f"{self.name}: {formatted_quantity} {self.unit.name}"

    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Ingredient):
            return False
        
        return self.name == other.name


    def __hash__(self) -> int:
        return hash(self.name)
