import pytest
from src.units.main.units import *

@pytest.mark.parametrize("unit_str, expected_unit", [
    ('g', MassUnits.GRAM),
    ('hg', MassUnits.HEKTOGRAM),
    ('kg', MassUnits.KILOGRAM),
    ('l', VolumeUnits.LITER),
    ('dl', VolumeUnits.DECILITER),
    ('cl', VolumeUnits.CENTILITER),
    ('ml', VolumeUnits.MILLILITER),
    ('msk', VolumeUnits.MATSKED),
    ('tsk', VolumeUnits.TESKED),
    ('krm', VolumeUnits.KRYDDMÅTT),
    ('st', CountUnits.STYCK),
])
def test_get_unit_from_string_valid_units(unit_str, expected_unit):
    assert get_unit_from_string(unit_str) == expected_unit


@pytest.mark.parametrize("unit_str", [
    'G', 'HG', 'KG', 'L', 'DL', 'CL', 'ML', 'MSK', 'TSK', 'KRM', 'ST'
])
def test_get_unit_from_string_case_insensitivity(unit_str):
    # This test checks if the function correctly handles uppercase inputs
    # It assumes that the function will not raise an error for valid unit strings
    try:
        get_unit_from_string(unit_str)
        assert True  # If no error is raised, the test passes
    except ValueError:
        assert False  # If an error is raised, the test fails


def test_get_unit_from_string_invalid_unit():
    with pytest.raises(ValueError):
        get_unit_from_string('invalid_unit')
