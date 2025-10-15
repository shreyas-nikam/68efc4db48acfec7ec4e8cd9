import pytest
from definition_08aeb7e23358405294192dd327543556 import calculate_ai_enhancement_potential

@pytest.mark.parametrize("ai_enhancement_score, expected", [
    (0.5, 0.5),  # Typical case
    (0.0, 0.0),  # Edge case: Minimum score
    (1.0, 1.0),  # Edge case: Maximum score
    (0.75, 0.75), # Another typical case
    (-0.5, -0.5), # Negative value
])
def test_calculate_ai_enhancement_potential(ai_enhancement_score, expected):
    assert calculate_ai_enhancement_potential(ai_enhancement_score) == expected