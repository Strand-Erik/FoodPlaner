import pytest
from src.models.main.ingredient import Ingredient
from src.units.main.units import *


@pytest.mark.parametrize("initial_quantity, initial_unit, expected_quantity, expected_unit", [
    (1500, MassUnits.GRAM, 1.5, MassUnits.KILOGRAM),
    (900, MassUnits.GRAM, 9, MassUnits.HEKTOGRAM),  # Adjusted to reflect the new normalization logic
    (1000, VolumeUnits.MILLILITER, 1, VolumeUnits.LITER),
    (15, VolumeUnits.MILLILITER, 1, VolumeUnits.MATSKED),  # Example where conversion to MATSKED is appropriate
    (5, VolumeUnits.MILLILITER, 1, VolumeUnits.TESKED),  # Example where conversion to TESKED is appropriate
    (1, VolumeUnits.MILLILITER, 1, VolumeUnits.KRYDDMÅTT),  # Example for KRYDDMÅTT normalization
    (250, MassUnits.GRAM, 2.5, MassUnits.HEKTOGRAM),  # Testing conversion to a non-base mass unit
    (110, VolumeUnits.MILLILITER, 1.1, VolumeUnits.DECILITER),  # Testing conversion to a non-base volume unit
])

def test_normalize_units(initial_quantity, initial_unit, expected_quantity, expected_unit):
    ingredient = Ingredient("Test Ingredient", initial_quantity, initial_unit)
    assert ingredient.quantity == expected_quantity
    assert ingredient.unit == expected_unit


def test_incompatible_units_addition():
    ingredient1 = Ingredient("Sugar", 1, MassUnits.KILOGRAM)
    ingredient2 = Ingredient("Water", 1, VolumeUnits.LITER)
    with pytest.raises(ValueError):
        result = ingredient1 + ingredient2


def test_different_ingredient_names():
    ingredient1 = Ingredient("Salt", 100, MassUnits.GRAM)
    ingredient2 = Ingredient("Sugar", 100, MassUnits.GRAM)
    with pytest.raises(ValueError):
        result = ingredient1 + ingredient2
        
        
@pytest.mark.parametrize("initial_quantity, initial_unit, added_quantity, added_unit, expected_quantity, expected_unit", [
    (500, MassUnits.GRAM, 1500, MassUnits.GRAM, 2, MassUnits.KILOGRAM),  # Testing conversion after addition
    (1.75, VolumeUnits.LITER, 250, VolumeUnits.MILLILITER, 2, VolumeUnits.LITER),  # Adding different units
    (2, CountUnits.STYCK, 3, CountUnits.STYCK, 5, CountUnits.STYCK),  # Testing simple countable addition
])

def test_addition_with_conversion(initial_quantity, initial_unit, added_quantity, added_unit, expected_quantity, expected_unit):
    ingredient1 = Ingredient("Test Ingredient", initial_quantity, initial_unit)
    ingredient2 = Ingredient("Test Ingredient", added_quantity, added_unit)
    result = ingredient1 + ingredient2
    assert result.quantity == expected_quantity
    assert result.unit == expected_unit


@pytest.mark.parametrize("initial_quantity, initial_unit, subtracted_quantity, subtracted_unit, expected_quantity, expected_unit", [
    (2, MassUnits.KILOGRAM, 250, MassUnits.GRAM, 1.75, MassUnits.KILOGRAM),  # Subtracting and keeping unit
    (2, VolumeUnits.LITER, 500, VolumeUnits.MILLILITER, 1.5, VolumeUnits.LITER),  # Subtracting different units
    (5, CountUnits.STYCK, 2, CountUnits.STYCK, 3, CountUnits.STYCK),  # Testing simple countable subtraction
])

def test_subtraction_with_conversion(initial_quantity, initial_unit, subtracted_quantity, subtracted_unit, expected_quantity, expected_unit):
    ingredient1 = Ingredient("Test Ingredient", initial_quantity, initial_unit)
    ingredient2 = Ingredient("Test Ingredient", subtracted_quantity, subtracted_unit)
    result = ingredient1 - ingredient2
    assert result.quantity == expected_quantity
    assert result.unit == expected_unit
