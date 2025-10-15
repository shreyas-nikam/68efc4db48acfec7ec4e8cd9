import pytest
from definition_793ea50a12ff42ca8f332ae016242283 import calculate_ai_fluency

@pytest.mark.parametrize("s1, s2, s3, s4, expected", [
    (0.8, 0.7, 0.9, 0.6, 0.76),  # Typical case
    (0.0, 0.0, 0.0, 0.0, 0.0),  # All skills zero
    (1.0, 1.0, 1.0, 1.0, 1.0),  # All skills perfect
    (-0.5, 0.7, 0.9, 0.6, -0.01), # Negative s1 should still function
    (0.8, 0.7, 0.9, 1.5, 0.86),   # s4 higher than 1 should still function
])
def test_calculate_ai_fluency(s1, s2, s3, s4, expected):
    assert round(calculate_ai_fluency(s1, s2, s3, s4), 2) == round(expected, 2)