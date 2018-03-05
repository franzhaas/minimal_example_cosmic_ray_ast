from itertools import repeat, chain
from typing import Sequence, Iterable, List, Callable, Any, Type
from functools import wraps



def _check_value(item: int) -> int:
    if item & 0xFF != item:
        raise ValueError('Trying to mem dump non byte data (0x00 - 0xFF)')
    return item

def transform_sequence_of_bytes_to_string_represented_mem(data: Iterable[int]) -> str:
    return ' '.join('{:02X}'.format(_check_value(item)) for item in data)


def transform_string_represented_mem_to_int_sequence(string_rep: str) -> List[int]:
    return [int(item, 16) for item in string_rep.split()]
