from hypothesis import given, example
from hypothesis.strategies import integers, lists

import mini


@given(lists(integers(min_value=0x00, max_value=0xFF)))
def test_reversible_sequence_conv(data):
    string_rep = mini.transform_sequence_of_bytes_to_string_represented_mem(data)
    assert data == mini.transform_string_represented_mem_to_int_sequence(string_rep)
