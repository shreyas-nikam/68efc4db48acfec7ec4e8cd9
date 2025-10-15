import pytest
from definition_f51e9a167bb943d3817f66deaf414161 import calculate_timing_factor

@pytest.mark.parametrize("years_experience, expected", [
    (5, 1 + (5/5)),
    (0, 1),
    (10, 1 + (10/5)),
    (-2, 1),
    (2.5, 1 + (2.5/5)),
])
def test_calculate_timing_factor(years_experience, expected):
    assert calculate_timing_factor(years_experience) == expected