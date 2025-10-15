import pytest
from definition_83faeb7bd371486b8c7324277e0438e8 import calculate_domain_expertise

@pytest.mark.parametrize("education_foundation, practical_experience, specialization_depth, expected", [
    (0.8, 0.7, 0.9, 0.79375),  # Typical case
    (0.0, 0.0, 0.0, 0.0),  # All inputs zero
    (1.0, 1.0, 1.0, 1.0),  # All inputs max
    (0.5, 0.5, 0.5, 0.5),  # All inputs at the midpoint
    (0.2, 0.9, 0.4, 0.44375),  # Varying inputs
])
def test_calculate_domain_expertise(education_foundation, practical_experience, specialization_depth, expected):
    assert calculate_domain_expertise(education_foundation, practical_experience, specialization_depth) == expected
