from enum import Enum, unique

INPUT_CITIES = {
    'SYD',
    'MEL',
    'ADL',
    'PER',
    'BLR',
    'DEL',
    'HYD',
    'SFO',
    'JFK',
    'ORD'
}


@unique
class Condition(Enum):
    Overcast = 0
    Rain = 1
    Snow = 2
    Sunny = 3


CONDITIONS_LIST = [name for name in Condition.__members__.items()]

NUM_DAYS = 365 * 11


def val(condition):
    return Condition[condition].value

