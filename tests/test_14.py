import pytest
from definition_829e8ff19a88497c9a1a841c57ec1525 import calculate_entry_accessibility

@pytest.mark.parametrize("education_years_required, experience_years_required, expected", [
    (4, 2, 1 / (1 + 0.1 * (4 + 2))),
    (0, 0, 1),
    (8, 5, 1 / (1 + 0.1 * (8 + 5))),
    (1, 0, 1 / (1 + 0.1 * (1 + 0))),
    (0, 1, 1 / (1 + 0.1 * (0 + 1)))
])
def test_calculate_entry_accessibility(education_years_required, experience_years_required, expected):
    assert calculate_entry_accessibility(education_years_required, experience_years_required) == expected