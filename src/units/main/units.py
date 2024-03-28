from enum import Enum
from typing import Optional

class MassUnits(Enum):
    KILOGRAM = 1000
    HEKTOGRAM = 100
    GRAM = 1


class VolumeUnits(Enum):
    LITER = 1000
    DECILITER = 100
    CENTILITER = 10
    MATSKED = 15
    TESKED = 5
    MILLILITER = 1
    KRYDDMÅTT = 1


class CountUnits(Enum):
    STYCK = 1  # 'Piece' or 'countable items', no conversion factor needed


BASE_UNITS = {
    MassUnits: MassUnits.GRAM,
    VolumeUnits: VolumeUnits.MILLILITER,
    CountUnits: CountUnits.STYCK
}


def get_base_unit(unit_enum):
    for unit_type, base_unit in BASE_UNITS.items():
        if isinstance(unit_enum, unit_type):
            return base_unit
    raise ValueError("Unknown unit type")


def get_unit_from_string(unit_str: str) -> Enum:
    unit_str = unit_str.lower()  # Ensure the unit string is lowercase for comparison
    unit_map = {
        'g': MassUnits.GRAM,
        'hg': MassUnits.HEKTOGRAM,
        'kg': MassUnits.KILOGRAM,
        'l': VolumeUnits.LITER,
        'dl': VolumeUnits.DECILITER,
        'cl': VolumeUnits.CENTILITER,
        'ml': VolumeUnits.MILLILITER,
        'msk': VolumeUnits.MATSKED,
        'tsk': VolumeUnits.TESKED,
        'krm': VolumeUnits.KRYDDMÅTT,
        'st': CountUnits.STYCK,
    }
    
    if unit := unit_map.get(unit_str, None):
        return unit
    else:
        raise ValueError(f"No unit matched with: {unit_str}")
