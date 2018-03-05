from hypothesis import given, example
from hypothesis.strategies import integers, lists

import mini
import sys

sys.setrecursionlimit(3000)

@given(integers(min_value=0x00, max_value=0xFF),integers(min_value=0x00, max_value=0xFF))
def test_reversible_sequence_conv(a, b):
    assert a + b == mini.adding(a, b)
