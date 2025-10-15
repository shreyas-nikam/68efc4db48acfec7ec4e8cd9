import pytest
from definition_25fcf376cdad4ca39b12ad766251d469 import calculate_growth_multiplier

@pytest.mark.parametrize("current, previous, lambda_val, expected", [
    (100, 50, 0.3, 1.6),  # Typical growth scenario
    (50, 100, 0.3, 0.65), # Contraction scenario
    (100, 100, 0.3, 1.0),  # No growth
    (0, 50, 0.3, 0.0),  # No current postings
    (100, 0, 0.3, 1.0), # previous is zero case
])
def test_calculate_growth_multiplier(current, previous, lambda_val, expected):
    assert calculate_growth_multiplier(current, previous, lambda_val) == expected